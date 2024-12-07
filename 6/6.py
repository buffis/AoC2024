from collections import *

f = open("in.txt").read()
l = f.find("\n")

pos = f.find("^")
curdir = "^"
nextdir = {">": "v", "v": "<", "<": "^", "^": ">"}
visited = defaultdict(set)

def get_next_pos(curdir, pos):
  match(curdir):
    case "^": return pos-l-1
    case "v": return pos+l+1
    case ">": return pos+1
    case "<": return pos-1

def is_oob(pos): return pos >= len(f) or pos < 0 or f[pos] == "\n"

# Part 1.
while True:
  nexpos = get_next_pos(curdir, pos)
  visited[pos].add(curdir)
  if is_oob(nexpos): break
  match(f[nexpos]):
    case "." | "^": pos = nexpos
    case "#":       curdir = nextdir[curdir]
print (len(visited))

# Part 2
part1visited, cnt = visited, 0
for i in part1visited:
  pos = f.find("^")
  f2 = f[:i] + "#" + f[i+1:]
  curdir = "^"
  visited = defaultdict(set)

  while True:
    nexpos = get_next_pos(curdir, pos)
    visited[pos].add(curdir)
    if is_oob(nexpos):
      break
    match(f2[nexpos]):
      case "." | "^": pos = nexpos
      case "#":       curdir = nextdir[curdir]
    if curdir in visited[nexpos]:
      cnt += 1
      break
print (cnt)
