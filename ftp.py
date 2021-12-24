import os
from ftplib import FTP

from settings import FTP_SERVER


def copy(src_path, dest_dir):
    ftp = FTP(FTP_SERVER)
    ftp.login()

    _, filename = os.path.split(src_path)
    with open(src_path, "rb") as src:
        ftp.storbinary(f"STOR {dest_dir}/{filename}", src)
    ftp.close()
