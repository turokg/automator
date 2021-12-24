#! /usr/local/bin/python3
import logging
import os
import os.path
import os.path
import re
import shutil
import time
from ftplib import FTP
from pathlib import Path

FTP_SERVER = '192.168.1.1'

FILTER_RE = re.compile(r".+torrent")
LEAVE_RE = re.compile(r".*ol.*")

SOURCE_DIR = Path("/Users/ek/Downloads/")
ARCHIVE_DIR = SOURCE_DIR / "archive/"
DESTINATION_DIR = Path("MOVIES/watch/")
CHECK_PERIOD = 5

if not os.path.exists(ARCHIVE_DIR):
    os.mkdir(ARCHIVE_DIR)

logger = logging.getLogger(__name__)


def copy(src_path, dest_dir):
    ftp = FTP(FTP_SERVER)
    ftp.login()

    _, filename = os.path.split(src_path)
    with open(src_path, "rb") as src:
        ftp.storbinary(f"STOR {dest_dir}/{filename}", src)
    ftp.close()


def handle(*files, destination):
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


def check_for_files(dir_, filter_re, leave_re):
    files = os.listdir(dir_)
    target_files = [dir_ / f for f in files if
                    filter_re.match(f) and not leave_re.match(f)]
    return target_files


def main():
    while True:
        logger.info("running loop")
        files = check_for_files(SOURCE_DIR, FILTER_RE, LEAVE_RE)
        handle(*files, destination=DESTINATION_DIR)
        time.sleep(CHECK_PERIOD)


if __name__ == "__main__":
    logging.basicConfig(
        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
        datefmt='%H:%M:%S',
        level=logging.DEBUG)
    main()
