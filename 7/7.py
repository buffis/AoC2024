def concat(x, y): return int(str(x) + str(y))

def calc(result, cur, rest, part2=False):
  if len(rest) == 0: return result if cur == result else 0
  elif cur > result: return 0  # Optimization. Not really needed.
  return calc(result, cur + rest[0], rest[1:], part2) or \
         calc(result, cur * rest[0], rest[1:], part2) or \
         (part2 and calc(result, concat(cur, rest[0]), rest[1:], part2))
      
f = open("input.txt").readlines()
sum1, sum2 = 0, 0
for line in f:
  result, nums = line.strip().split(":")
  result, nums = int(result), list(map(int, nums.strip().split()))
  sum1 += calc(result, nums[0], nums[1:])
  sum2 += calc(result, nums[0], nums[1:], part2=True)
print("Part1", sum1, "\nPart2", sum2)
