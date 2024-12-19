import re
f = open("input.txt").readlines()
regex = '^(' + f[0].strip().replace(', ', '|') + ')*$'
print (sum(1 for line in f[2:] if (re.match(regex, line))))
