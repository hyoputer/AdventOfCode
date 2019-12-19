import re
import copy
import math

def lcm(x, y):
  return (x*y)//math.gcd(x, y)

posl = []
rposl = []
for i in range(4):
  line = input()

  l = list(map(int, re.findall("-{0,1}\d+", line)))
  posl.append(l)
  
vell = [[0 for i in range(3)] for i in range(4)]
cycle = [0 for i in range(3)]
b_c = [False for i in range(3)]

num = 0
while True:
      
  for i in range(4):
    for j in range(i+1, 4):
      for k in range(3):
        if posl[i][k] < posl[j][k]:
          vell[i][k] += 1
          vell[j][k] -= 1
        elif posl[i][k] > posl[j][k]:
          vell[i][k] -= 1
          vell[j][k] += 1

  for i in range(4):
    for j in range(3):
      posl[i][j] += vell[i][j]
      
  num += 2
  
  for i in range(3):
    if not b_c[i]:
      zf = True
      for j in range(4):
        if vell[j][i] != 0:
          zf = False
          break
          
      if zf:
        b_c[i] = True
        cycle[i] = num
  
  f = True
  
  for i in range(3):
    if not b_c[i]:
      f = False
      break
  
  if f:
    break
    
print(lcm(lcm(cycle[0], cycle[1]), cycle[2]))