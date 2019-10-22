import urllib3
import logging
import logging.config
from pathlib import Path

logging.config.fileConfig('logging.conf')
# create logger
logger = logging.getLogger('ctext')


def download(file_num):
    pool = urllib3.PoolManager()
    title = "三國志通俗演義"
    sino_index = 0

    while file_num <= 72:
        if sino_index < 24:
            sino_count = get_sino_count(sino_index)
        else:
            break

        file_name = title + sino_count + ".pdf"
        path = Path(title)

        if not path.exists():
            path.mkdir();
            logging.info("已作成：" + title)

        # file = Path(file_name)
        file_path = path / file_name

        if not file_path.is_file():
            url = "https://ia800502.us.archive.org/0/items/021117{num}.cn/021117{num}.cn.pdf"
            url = url.format(num = file_num)
            # Download the data
            logging.info("下載：" + url)
            response = pool.request("GET", url)
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

def get_sino_count(sino_index):
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

if __name__ == "__main__":
    init_num = 49
    download(init_num)

