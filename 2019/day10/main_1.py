import sys

aster = []

for line in sys.stdin:
  lline = list(line.rstrip())
  aster.append(lline)
  
res = 0


def check(li, y, x, q, p):
  for e in li:
    if x == p:
      if e[0] == 1e9 and ((q>y and e[1] == '+') or (q<y and e[1] == '-')):
        return False
      else:
        pass
    elif (q-y)/(p-x) == e[0] and ((p>x and e[1] == '+') or (p<x and e[1] == '-')):
      return False
    
  return True
    
                      
for i in range(len(aster)):
  for j in range(len(aster[0])):
    if(aster[i][j] == '#'):
      cklist = []
      
      for k in range(len(aster)):
        for l in range(len(aster[0])):
          if aster[k][l] == '#' and (i != k or j != l):
            f = check(cklist, i, j, k, l)
            
            if f:
              if j == l:
                if k > i:
                  cklist.append((1e9, '+'))
                else:
                  cklist.append((1e9, '-'))
              else:
                if l > j:
                  cklist.append(((k-i)/(l-j), '+'))

                elif l < j:
                  cklist.append(((k-i)/(l-j), '-'))
              
      res = max(res, len(cklist))
      if len(cklist) == 278:
        print(i)
        print(j)
      
print(res)