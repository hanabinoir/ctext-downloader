import urllib3
import logging
import logging.config

import downloader

from pathlib import Path


if __name__ == "__main__":
    title = "三國志通俗演義"
    init_file_num = 49
    max_file_num = 72
    dl = downloader.Downloader(title, init_file_num, max_file_num)
    dl.download()