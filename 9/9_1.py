# Part 1
# Not cleaned up at all. Part 2 looks nicer.

f = open("input.txt").read().strip()
d = []
fid = 0
isfile = 1
for i, c in enumerate(f):
   if isfile:
       for j in range(int(c)):
           d.append(str(fid))
       fid += 1
   else:
       for j in range(int(c)):
           d.append(".")
   isfile = not isfile
print ("".join(d))
print ("sdasd")
i,j = 0, len(d)-1
while j > i:
  if d[j] == ".":
    j-=1
    continue
  if d[i] != ".":
    i+=1
    continue
  d[i],d[j] = d[j],d[i]
  i += 1
  j -= 1
print ("".join(d))
s = 0
for i,x in enumerate(d):
  if x == ".": break
  s += int (i)*int(x) 
print (s)
