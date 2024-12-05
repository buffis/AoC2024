import re

def middle(x): return x[len(x)//2]

# Part 1
rval, regex = 0, "XMAS"
for line in open("in.txt").readlines():
    if "|" in line:
        x = line.strip().split("|")
        regex += r"|((^|,)%s,(\d+,)*%s($|,))" % (x[1], x[0])
    elif not re.search(regex, line) and line.strip():
        rval += int(middle(line.strip().split(",")))
print ("Part1", rval)

# Part 2 (reuses generated regex from above)
rval = 0
for line in open("in.txt").readlines():
    if "|" not in line and re.search(regex, line):
        r, x = [], line.strip().split(",")
        for y in x:
            for i in range(len(r) + 1):
                r2 = r[:i] + [y] + r[i:]
                if not re.search(regex, ",".join(r2)):
                    r = r2
                    break
        rval += middle([int(x) for x in r])
print ("Part2", rval)
                    

