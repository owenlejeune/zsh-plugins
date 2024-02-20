import sys
from random import randint

check_start = False
prefix = ''
num = 1

if len(sys.argv) == 1:
    print("ERROR: Please include a filename")
    print("Usage: frand <FILENAME> [<INCLUDES>] [n=<NUM>]")
    sys.exit(0)

fn = sys.argv[1]

for i in range(2, len(sys.argv)):
    if sys.argv[i].startswith("n="):
        num = int(sys.argv[i][2:])
    else:
        prefix = sys.argv[i]
        check_start = True


lines = []
with open(fn) as f:
    for line in f:
        nline = line.replace("\n", "")
        lines.append(nline)

for x in range(0, num):
    if check_start:
        line_sub = []
        for i in lines:
            if i.startswith(prefix):
                line_sub.append(i)
        numitems = len(line_sub)
        i = randint(0,numitems-1)
        print(line_sub[i])
    else:
        numitems = len(lines)
        i = randint(0,numitems-1)
        print(lines[i])
