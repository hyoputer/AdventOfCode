import sys
import heapq
import math

aster = []

for line in sys.stdin:
  lline = list(line.rstrip())
  aster.append(lline)
  
MS = [19,23]

#print(MS)

def check(li, y, x, q, p):
  for e in li:
    if p < x:
      if math.atan2(p-x, y-q) + 7 == e[0]:
        heapq.heappush(e[1], ((q-y)*(q-y) + (p-x)*(p-x), (q, p)))
        return False
    elif math.atan2(p-x, y-q) == e[0]:
      heapq.heappush(e[1], ((q-y)*(q-y) + (p-x)*(p-x), (q, p)))
      return False
      
  return True
    
                      
cklist = []

for k in range(len(aster)):
  for l in range(len(aster[0])):
    if aster[k][l] == '#' and (MS[0] != k or MS[1] != l):
      f = check(cklist, MS[0], MS[1], k, l)

      if f:
        key = 0
        if l < MS[1]:
          key = math.atan2(l-MS[1], MS[0]-k) + 7 # y <--> x
        else:
          key = math.atan2(l-MS[1], MS[0]-k)
        cklist.append((key, [((MS[0]-k)*(MS[0]-k) + (MS[1]-l)*(MS[1]-l), (k, l))]))

cklist.sort(key=lambda tp:tp[0])

#print(cklist)

while True:
  for e in cklist:
    if not e[1]:
      continue
    print(heapq.heappop(e[1])[1])