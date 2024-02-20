from random import randrange
import sys

#num = int(input("Enter a number: "))
#num2 = int(input("How many numbers: "))

args = len(sys.argv)
if args<3 or args>4:
    print("Invalid command\n  usage: randnums <MIN> <MAX> [<NUM>]")
    quit()

nmin = int(sys.argv[1])
nmax = int(sys.argv[2])
nnum = 1 if args==3 else int(sys.argv[3])

if nmin>=nmax:
    print("Error: min must be less than max")
    quit()
if nnum <= 0:
    print("Error: num must be greater than 0")
    quit()

for x in range(0, nnum):
    print(randrange(nmin, nmax))
