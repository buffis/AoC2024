d = {}

def stonesmade(x, n):
  if n == 0:       return 1
  elif (x,n) in d: return d[(x,n)]
  elif x == "0":
    d[(x,n)] = stonesmade("1", n-1)
  elif not len(x) % 2:
    d[(x,n)] = stonesmade(str(int(x[:len(x)//2])), n-1) + \
               stonesmade(str(int(x[len(x)//2:])), n-1)
  else:
    d[(x,n)] = stonesmade(str(int(x)*2024), n-1)
  return d[(x,n)]

f=open("input.txt").read().strip().split()
print(sum(stonesmade(x, 75) for x in f))
