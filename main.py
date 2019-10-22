import urllib3
import logging
import logging.config

import downloader
import interface

from pathlib import Path


if __name__ == "__main__":
    # Get download parameters from input
    parameters = interface.Interface()
    title = parameters.get_title()
    init_file_str = parameters.get_init_file_str()
    max_file_str = parameters.get_max_file_str()

    # Download the files
    dl = downloader.Downloader(title, init_file_str, max_file_str)
    dl.download()