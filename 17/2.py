import re
f=open("input.txt").read()
regex = r".*: (.*)\n.*: (.*)\n.*: (.*)\n\n.*:(.*)"
indata = re.findall(regex,f)[0]
program = list(map(int, indata[3].split(",")))
a, b, c = map(int, indata[:3])
ip = 0
output = []

def combo(x):
  if x <= 3: return x
  if x == 4: return a
  if x == 5: return b
  if x == 6: return c

def adv(x):
  global a
  a = a // (2 ** combo(x))

def bxl(x):
  global b
  b = b ^ x

def bst(x):
  global b
  b = combo(x) & 0b111

def jnz(x):
  global ip
  if a:
    ip = x - 2  # will be x, post increment

def bxc(x):
  global b
  b = b ^ c

def out(x):
  global output
  output.append(combo(x) & 0b111)

def bdv(x):
  global b
  b = a // (2 ** combo(x))

def cdv(x):
  global c
  c = a // (2 ** combo(x))

ops = {0: adv, 1: bxl, 2: bst, 3: jnz, 4: bxc, 5: out, 6: bdv, 7: cdv}

def run(p, a_override=None):
  global ip, output, a, b, c
  a, b, c = map(int, indata[:3])
  a = a_override if a_override else a
  ip = 0
  output = []
  while ip < len(program):
    op, arg = program[ip:ip+2]
    ops[op](arg)
    ip += 2
  return output

cool_a = 0
for j, p in enumerate(program):
  for i in range(1024):
    a2 = cool_a | i
    if run(program, a2) == program[-j-1:]:
      cool_a = a2 << 3
print (cool_a>>3)
