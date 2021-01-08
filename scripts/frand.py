import os, os.path
import sys
from random import randint

dirn = sys.argv[1]
dirlist = os.listdir(dirn)
numitems = len(dirlist)
i = randint(0,numitems-1)
print(dirlist[i])

