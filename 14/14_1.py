import re
from collections import defaultdict
from operator import mul
from functools import reduce

f = open('input.txt').read()
sizex, sizey, ticks = 101, 103, 100
regex = r'p.(.+),(.+) v.(.+),(.+)'
quads = defaultdict(int)

def add_quadrant(x,y):
  if x < sizex // 2:
    if y < sizey // 2:
      quads[1] += 1
    elif y > sizey // 2:
      quads[2] += 1
  elif x > sizex // 2:
    if y < sizey // 2:
      quads[3] += 1
    elif y > sizey // 2:
      quads[4] += 1

for matches in re.findall(regex, f):
  px, py, vx, vy = map(int, matches)
  x = (px + vx * ticks) % sizex
  y = (py + vy * ticks) % sizey
  add_quadrant(x,y)

print (reduce(mul, quads.values()))
