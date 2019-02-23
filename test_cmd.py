# run as --> python test_cmd.py 10 20
# -- practise


# program to add two numbers using command line argumnets--
# --  run on cmd and pass command line arguments..
import sys

print(sys.argv)
def printsum():
    print(int(sys.argv[1])+int(sys.argv[2]))
printsum()
