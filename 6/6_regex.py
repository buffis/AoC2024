# Alternative solution for Part 1 with regex
import re

f = open("test.txt").read()
l = f.find("\n")

regex = [(">#", "v#"), (r"v(.{%d})#" % l, r"<\1#"),
         ("#<", r"#^"), (r"#(.{%d})\^" % l, r"#\1>"),
         (">([.X])", r"X>"), (r"v(.{%d})[.X]" % l, r"X\1v"),
         ("[.X]<", r"<X"), (r"[.X](.{%d})\^" % l, r"^\1X")]
changed = True
while changed:
  changed = False
  for r in regex:
    if re.search(r[0], f, flags=re.S):
      f = re.sub(r[0], r[1], f, count=1, flags=re.S)
      changed = True
f = re.sub(r"[v\^<>]", "X", f)
print (f, "\n", f.count("X"))
