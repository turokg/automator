#! /usr/local/bin/python3
import logging
import os.path
import shutil
import time

from ftp import copy
from settings import (
    ARCHIVE_DIR, CHECK_PERIOD, DESTINATION_DIR, FILTER_RE, FTP_SERVER,
    SOURCE_DIR,
    )

logger = logging.getLogger(__name__)


def move(destination, *files):
    for file_ in files:
        try:
            copy(file_, destination)
            logger.debug("copied %s to %s @ %s", file_, destination,
                         FTP_SERVER)
        except Exception as e:
            logger.debug("couldn't copy file: %s", e)
        else:
            shutil.move(file_, ARCHIVE_DIR)
            logger.debug("moved %s to %s", file_, ARCHIVE_DIR)


def check_for_files(dir_, filter_re):
    files = os.listdir(dir_)
    target_files = [dir_ / f for f in files if filter_re.match(f)]
    return target_files


def main():
    while True:
        logger.info("running loop")
        files = check_for_files(SOURCE_DIR, FILTER_RE)
        move(DESTINATION_DIR, *files)
        time.sleep(CHECK_PERIOD)


if __name__ == "__main__":
    logging.basicConfig(
        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
        datefmt='%H:%M:%S',
        level=logging.DEBUG)
    main()
