import re
from operator import *

# Part 1
data = open("in.txt").read()
print (sum(eval(x) for x in re.findall(r"mul\(\d+,\d+\)", data)))

# Part 2
print (sum(map(eval, re.findall("mul\(\d+,\d+\)",
    re.sub("don't\(\)((?s:.)*?do\(\)|(?s:.)*)",
           ".",
           open("in.txt").read())))))
