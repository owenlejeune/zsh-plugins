import os
import sys
import pathlib
import datetime

dirn = sys.argv[1]
dirlist = os.listdir(dirn)

dates = []

for f in dirlist:
    if f[:1] != '.' and os.path.isfile(dirn + "/" + f):
        fname = pathlib.Path(dirn + "/" + f)
        ctime = datetime.datetime.fromtimestamp(fname.stat().st_ctime)
        date = str(ctime)[:10]
        if date not in dates:
            if not os.path.isdir(dirn + "/" + date):
                dates.append(date)
                os.mkdir(dirn + "/" + date)
        os.rename(dirn + "/" + f, dirn + "/" + date + "/" + f)
