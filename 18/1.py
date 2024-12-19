lines = open("input.txt").readlines()
maxx, maxy = 70, 70
m = {}
for i, line in enumerate(lines):
  if i == 1024: break
  x,y = map(int, line.strip().split(","))
  m[(x, y)] = -1

active = [(0,0)]
m[0,0] = 0
while active:
  x, y = active.pop(0)
  if x == maxx and y == maxy:
    break
  for x2, y2 in [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]:
    if x < 0 or y < 0 or x > maxx or y > maxy: continue
    if not (x2, y2) in m:
      active.append((x2, y2))
      m[(x2, y2)] = m[(x, y)] + 1

print (m[(maxx, maxy)])
