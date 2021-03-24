import os, os.path
import sys
from random import randint

check_start = False
start = ''

dirn = sys.argv[1]

if len(sys.argv) > 2:
    start = sys.argv[2]
    check_start = True

dirlist = os.listdir(dirn)

if check_start:
    fs = []
    for i in dirlist:
        if i.startswith(start):
            fs.append(i)
    numitems = len(fs)
    found = False
    while not found:
        j = randint(0,numitems-1)
        if fs[j][0] != ".":
            found = True
    print(fs[i])
else:
    numitems = len(dirlist)
    found = False
    while not found:
        i = randint(0,numitems-1)
        if dirlist[i][0] != ".":
            found = True
    # i = randint(0,numitems-1)
    print(dirlist[i])
