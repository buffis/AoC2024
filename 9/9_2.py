# Part 2
f = open("input.txt").read().strip()
d, files, gaps = [], {}, []
fid, isfile = 0, True
for i, c in enumerate(f):
  if isfile:
    files[fid] = (len(d), int(c))
    d.extend([fid] * int(c))
    fid += 1
  else:
    gaps.append((len(d), int(c)))
    d.extend([-1] * int(c))
  isfile = not isfile
for fid in reversed(range(fid)):
  file = files[fid]
  for gapid, gap in enumerate(gaps):
    if gap[0] < file[0] and gap[1] >= file[1]:
      for i in range(file[1]):
        d[gap[0]+i] = d[file[0]+i]
        d[file[0]+i] = -1
      gaps[gapid] = (gap[0]+file[1], gap[1]-file[1])
      break
s = sum([i*x for (i, x) in enumerate(d) if x != -1])
print (s)
