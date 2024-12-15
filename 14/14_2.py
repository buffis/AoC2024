import re
from collections import defaultdict

f = open('input.txt').read()
sizex, sizey, ticks = 101, 103, 100
regex = r'p.(.+),(.+) v.(.+),(.+)'

for ticks in range(0,50000):
  xd, yd = defaultdict(int), defaultdict(int)
  for matches in re.findall(regex, f):
    px, py, vx, vy = map(int, matches)
    x = (px + vx * ticks) % sizex
    y = (py + vy * ticks) % sizey
    xd[x] += 1
    yd[y] += 1
    if xd[x] > 20 and yd[y] > 20:
      print (ticks)
