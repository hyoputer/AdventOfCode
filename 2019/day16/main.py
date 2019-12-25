import math

def part1(llist, pat):
  length = len(llist)
  for num in range(100):
    res = [0 for i in range(length)]
    for i in range(length):
      for j in range(length):
        res[i] += int(llist[j]) * pat[(math.floor((j+1)/(i+1)))%4]
       # print((math.floor((j+1)/(i+1)))%4)

      res[i] = int(str(res[i])[len(str(res[i]))-1])
    llist = res
    #print(res)
    
  return res

def part2(llist):
  length = len(llist)
  llist *= 10000
  offset = int(''.join(llist[:7]))
  for num in range(100):
    res = [0 for i in range(length*10000)]
    for i in range(length*10000-1, offset-1, -1):
      res[i] += int(llist[i]) + res[(i+1)%len(res)]
      res[i] = int(str(res[i])[len(str(res[i]))-1])
    llist = res
    
  return res[offset:offset+8]


line = input()

pat = [0,1,0,-1]

print(part1(list(line),pat))
print(part2(list(line)))