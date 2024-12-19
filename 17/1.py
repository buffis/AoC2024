import re

f=open("input.txt").read()
regex = r".*: (.*)\n.*: (.*)\n.*: (.*)\n\n.*:(.*)"
indata = re.findall(regex,f)[0]
a, b, c = map(int, indata[:3])
program = list(map(int, indata[3].split(",")))
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
  if a == 0: return
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

def run(p):
  global ip
  while ip < len(program):
    op, arg = program[ip:ip+2]
    ops[op](arg)
    ip += 2

run(program)

print (",".join(map(str, output)))


