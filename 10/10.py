from collections import defaultdict
from itertools import chain

f = open("input.txt").read()
l = f.find("\n")

def isoob(pos):
    return pos < 0 or pos >= len(f) or f[pos] == "\n"
def get_surround(pos):
    return [x for x in (pos-1, pos+1, pos-l-1, pos+l+1) if not isoob(x)]

# Build a map of node -> surrounding incremented nodes
d = defaultdict(lambda: defaultdict(list))
for pos, c in enumerate(f):
    if c != "\n" and c != ".":
        c = int(c)
        for x in get_surround(pos):
            if f[x] != "." and int(f[x]) == c+1:
                d[c][pos].append(x)

# Traverse map
def solve(part1 = True):
    s = 0
    for trailhead in d[0]:
        l = d[0][trailhead]
        for i in range(1, 10):
            hits = [x for x in d[i] if x in l] if part1 else  [x for x in l if x in d[i]]
            if i != 9:
                l = list(chain.from_iterable([d[i][hit] for hit in hits]))
            else:
                s += len(set(l)) if part1 else len(l)
    return s

print ("Part 1", solve(True), "\nPart 2", solve(False))