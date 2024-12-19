lines = open("in1.txt").readlines()
patterns = lines[0].strip().split(", ")

d = {}
def f(x):
    if x == "": return 1
    if x in d: return d[x]
    d[x] = sum(f(x[len(p):]) for p in patterns if x.startswith(p))
    return d[x]

print (sum(f(l.strip()) for l in lines[2:]))
