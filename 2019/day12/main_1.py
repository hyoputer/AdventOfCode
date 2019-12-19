import re

posl = []
rposl = []
for i in range(4):
  line = input()

  l = list(map(int, re.findall("-{0,1}\d+", line)))
  posl.append(l)
  
vell = [[0 for i in range(3)] for i in range(4)]

num = 0
for x in range(1000):
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
    
    
print(posl)
print(vell)

res = 0

for i in range(4):
  pot = 0
  kin = 0
  for j in range(3):
    pot += abs(posl[i][j])
    kin += abs(vell[i][j])
    
  res += pot*kin
  
print(res)