import collections

f=open("in1.txt").read()
x=list(map(int, sorted(f.split()[::2])))
y=list(map(int, sorted(f.split()[1::2])))

# Part 1
o=0
for i, j in zip(x, y):
  o += abs(i - j)
print(o)

# Part 2
d = collections.defaultdict(int)
o = 0
for i in y:
  d[i] += 1
for i in x:
  o += i * d[i]
print(o)
