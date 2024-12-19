lines = open("input.txt").readlines()
maxx, maxy = 70, 70

def run(steps):
  m = {(0, 0)}
  for i, line in enumerate(lines):
    if i < steps: 
      x, y = map(int, line.strip().split(","))
      m.add((x, y))

  active = [(0, 0)]
  while active:
    x, y = active.pop(0)
    if x == maxx and y == maxy:
      return True
    for x2, y2 in [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]:
      if x < 0 or y < 0 or x > maxx or y > maxy: continue
      if not (x2, y2) in m:
        active.append((x2, y2))
        m.add((x2, y2))

for i in range(len(lines)):
  if not run(i):
    print (lines[i-1])
    break


