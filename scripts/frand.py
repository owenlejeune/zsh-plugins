import sys
from random import randint

check_start = False
start = ''

fn = sys.argv[1]

if len(sys.argv) > 2:
    start = sys.argv[2]
    check_start = True

lines = []
with open(fn) as f:
    for line in f:
        nline = line.replace("\n", "")
        lines.append(nline)

if check_start:
    line_sub = []
    for i in lines:
        if i.startswith(start):
            line_sub.append(i)
    numitems = len(line_sub)
    i = randint(0,numitems-1)
    print(line_sub[i])
else:
    numitems = len(lines)
    i = randint(0,numitems-1)
    print(lines[i])
