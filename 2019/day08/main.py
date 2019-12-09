import sys

wide = sys.stdin.readline()
wide.rstrip()
w = int(wide)

tall = sys.stdin.readline()
tall.rstrip()
t = int(tall)

layer = int(wide) * int(tall)

line = sys.stdin.readline()
line.rstrip()
  
size = len(line)

i = layer

li = list(line[0:layer])

while i < size:
  for idx in range(layer):
    if li[idx] == '2' and line[i+idx] != '2':
      li.pop(idx)
      li.insert(idx, line[i+idx])
      
  i += layer
  
for i in range(t):
  for j in range(w):
    print(int(li[i*w + j]), end = '')
  print('\n')