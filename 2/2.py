def is_safe(x):
  y = [y[0] - y[1] for y in zip(x, x[1:])]
  return not [x for x in y if x<1 or x>3] \
      or not [x for x in y if x>-1 or x<-3]

def get_number_rows(filename):
  return [list(map(int, line.split())) for line in open(filename).readlines()]

# Part 1:
r = 0
for x in get_number_rows("in.txt"):
  if is_safe(x):
    r += 1
print (r)

# Part 2:
r = 0
for x in get_number_rows("in.txt"):
  for i in range(len(x)):
    y = x[:]
    del(y[i])
    if is_safe(y):
      r += 1
      break
print (r)
