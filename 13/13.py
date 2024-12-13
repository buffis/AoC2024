import re
import numpy

f = open('input.txt').read()
regex = r' X.(\d+), Y.(\d+).*? X.(\d+), Y.(\d+).*? X.(\d+), Y.(\d+)\b'
tokens = 0
for match in re.findall(regex, f, flags=re.DOTALL):
  ax, ay, bx, by, px, py = map(int, match)
  px += 10000000000000
  py += 10000000000000
  s = numpy.linalg.solve(
      numpy.array([[ax, bx], [ay, by]]),
      numpy.array([px, py]))
  ta, tb = round(s[0]), round(s[1])
  if (ta * ax + tb * bx == px) and (ta * ay + tb * by == py):
    tokens += ta * 3 + tb
print(tokens)
