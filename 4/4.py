import re
data = open("in.txt").read()
l = data.find("\n")

def count(r): return len(re.findall(r,data))

# Part 1
regex = r'(?=(?s:X$M$A$S|S$A$M$X))'
print(sum(count(regex.replace("$", ".{%d}" % x)) for x in (0, l-1, l, l+1)))

# Part 2
regex = r'(?=(?s:M.S$M.S|S.S$M.M|M.M$S.S|S.M$S.M))'.replace("$", ".{%d}A.{%d}" % (l-1, l-1))
print(count(regex))
