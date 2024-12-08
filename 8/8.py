from collections import defaultdict

f = open("input.txt").readlines()
maxx, maxy = len(f[0].strip()) - 1, len(f) - 1

def tsub(a, b): return (a[0]-b[0], a[1]-b[1])
def tadd(a, b): return (a[0]+b[0], a[1]+b[1])
def isoob(a): return a[0] < 0 or a[1] < 0 or a[0] > maxx or a[1] > maxy

def solve(is_part2 = False):
   nodes = defaultdict(list)
   for y, line in enumerate(f):
       for x, c in enumerate(line):
           if c != "." and c != "\n":
               nodes[c].append((y, x))

   antis = set()
   for nodelist in nodes.values():
       for a in nodelist:
           for b in nodelist:
               if a != b:
                   diff = tsub(a, b)
                   if not is_part2:
                       anti = tadd(a, diff)
                       if not isoob(anti):
                           antis.add(anti)
                   else:
                       anti = a
                       while not isoob(anti):
                           antis.add(anti)
                           anti = tadd(anti, diff)
                       while not isoob(anti):
                           antis.add(anti)
                           anti = tsub(anti, diff)
   return len(antis)

print ("Part 1", solve())
print ("Part 2", solve(True))
