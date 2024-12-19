f = open("input.txt").readlines()

field, hits, active = {}, {}, []
start, end = (0, 0), (0, 0)

def set_hit(x, y, d, steps):
  hits[(x,y,d)] = steps if not (x,y,d) in hits else min(hits[(x,y,d)], steps)

def get_hit(x, y, d):
  return hits[(x,y,d)] if (x,y,d) in hits else 99999999

# Read input
for y, line in enumerate(f):
  for x, c in enumerate(line):
    field[(x,y)] = c
    if c == "S":
        start = (x,y)
    if c == "E":
        end = (x,y)

# Traverse.
def move(x, y, d, steps):
  if (x,y) not in field or field[(x,y)] == "#": return

  if (x,y,d) not in hits or hits[(x,y,d)] > steps:
    active.append((x,y))
    match (d):
      case "e":
        set_hit(x,y,"e",steps)
        set_hit(x,y,"s",steps+1000)
        set_hit(x,y,"w",steps+2000)
        set_hit(x,y,"n",steps+1000)
      case "s":
        set_hit(x,y,"e",steps+1000)
        set_hit(x,y,"s",steps)
        set_hit(x,y,"w",steps+1000)
        set_hit(x,y,"n",steps+2000)
      case "w":
        set_hit(x,y,"e",steps+2000)
        set_hit(x,y,"s",steps+1000)
        set_hit(x,y,"w",steps)
        set_hit(x,y,"n",steps+1000)
      case "n":
        set_hit(x,y,"e",steps+1000)
        set_hit(x,y,"s",steps+2000)
        set_hit(x,y,"w",steps+1000)
        set_hit(x,y,"n",steps)

move(start[0],start[1],"e",0)
while active:
  active2 = active
  active = []
  for (x,y) in active2:
    move(x+1, y, "e", hits[(x,y, "e")] + 1)
    move(x, y+1, "s", hits[(x,y, "s")] + 1)
    move(x-1, y, "w", hits[(x,y, "w")] + 1)
    move(x, y-1, "n", hits[(x,y, "n")] + 1)

# Now lets go back!
backtracked = set()
def backtrack(x,y,d):
  steps = get_hit(x, y, d)
  backtracked.add((x,y))

  if d == "e" or d == "w":
    dx = x-1 if d == "e" else x+1
    if get_hit(dx, y, d) == (steps-1): backtrack(dx, y, d)
    if get_hit(x, y+1, "n") == (steps - 1001): backtrack(x,y+1,"n")
    if get_hit(x, y-1, "s") == (steps - 1001): backtrack(x,y-1,"s")
  else:
    dy = y-1 if d == "s" else y+1
    if get_hit(x, dy, d) == (steps-1): backtrack(x, dy, d)
    if get_hit(x+1, y, "w") == (steps - 1001): backtrack(x+1,y,"w")
    if get_hit(x-1, y, "e") == (steps - 1001): backtrack(x-1,y,"e")

enddir = sorted((get_hit(end[0], end[1], d), d) for d in "news")[0][1]
backtrack(end[0], end[1], enddir)

print (len(backtracked))
