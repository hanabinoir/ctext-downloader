import urllib3
import logging
import logging.config
from pathlib import Path

logging.config.fileConfig('logging.conf')
logger = logging.getLogger('ctext')


class Downloader():
    def __init__(self, title, init_file_str, max_file_str):
        self.title = title
        self.init_file_str = init_file_str
        self.max_file_str = max_file_str

    def download(self):
        title = self.title
        pool = urllib3.PoolManager()
        file_num = int(self.init_file_str)
        max_file_num = int(self.max_file_str)
        sino_index = 0
        max_sino_index = max_file_num - file_num + 1
        
        while file_num <= max_file_num:
            if sino_index < max_sino_index:
                sino_count = self.get_sino_count(sino_index)
            else:
                break

            file_name = title + sino_count + ".pdf"
            downloaded_root = Path('Downloaded')
            title_path_name = Path(title)
            title_path = downloaded_root / title_path_name
            file_path = downloaded_root / title_path_name / file_name

            if not title_path.exists():
                title_path.mkdir();
                logging.info("已作成：" + title)

            if not file_path.is_file():
                file_str = str(file_num)
                missed_digits = len(self.init_file_str) - len(file_str)
                leading_zeros = '0' * (missed_digits // len('0'))
                file_str = leading_zeros + file_str
                url = "https://ia800502.us.archive.org/0/items/{file_str}.cn/{file_str}.cn.pdf"
                url = url.format(file_str = file_str)
                # Download the data
                logging.info("下載：" + url)
                response = pool.request("GET", url)

                # Stop when the file does not exists
                if not response.status == 200:
                    logging.warning("文件不存在，下載中止")
                    break

                logging.info("下載完成：" + file_name) # Dowload finished

                # Created the pdf with the data
                logging.info("創建文件：" + file_name)
                file = open(file_path, 'wb')
                file.write(response.data)
                file.close()
                logging.info("創建完成：" + file_name) # Creation finished
            else:
                logging.warning("已存在：" + file_name) # File already exists
            
            sino_index += 1
            file_num += 1

    # Get the sino count for volumn
    def get_sino_count(self, sino_index):
        sino_counts = ["一", "二", "三", "四", "五", "六", "七", "八", "九", "十"]
        sino_count = ""
        remainder = sino_index % 10
        
        if sino_index < 19:
            if sino_index < 10:
                sino_count = sino_counts[sino_index]
            else:
                sino_count = "十" + sino_counts[remainder]
        else:
            tens_index = (int) (sino_index / 10)

            if remainder == 9:
                tens = sino_counts[tens_index]
                sino_count = tens + "十"
            else:
                tens_index -= 1
                tens = sino_counts[tens_index]
                sino_count = tens + "十" + sino_counts[remainder]

        return sino_count
        