import os.path
import re
from pathlib import Path

FTP_SERVER = '192.168.1.1'

FILTER_RE = re.compile(r".+torrent")
SOURCE_DIR = Path("/Users/ek/Downloads/")
ARCHIVE_DIR = SOURCE_DIR / "archive/"
DESTINATION_DIR = Path("MOVIES/watch/")
CHECK_PERIOD = 5

if not os.path.exists(ARCHIVE_DIR):
    os.mkdir(ARCHIVE_DIR)
