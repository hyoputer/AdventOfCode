import intcom

inline = input()

code_str = inline.split(',')

code = list(map(int, code_str))

com = intcom.intcomProgram(code)

m = [[0 for i in range(100)] for i in range(100)]
visited = [[0 for i in range(100)] for i in range(100)]

cur = [50, 50]
d = [[-1, 0], [0, 1], [1, 0], [0, -1]]
curd = 0

com.put_Input([1])

while not com.is_done():
  visited[cur[0]][cur[1]] = 1
  com.run()
  output = com.get_Output()
  m[cur[0]][cur[1]] = output.get()
  next = output.get()
  if next == 0:
    curd -= 1
  else:
    curd += 1
  curd %= 4
  temp = cur
  cur = [temp[0]+d[curd][0], temp[1]+d[curd][1]]
  com.put_Input([m[cur[0]][cur[1]]])
  
res = 0

for e1 in visited:
  for e2 in e1:
    if e2 == 1:
      res += 1
      
print (res)

for e1 in m:
  for e2 in e1:
    print(e2, end='')
  print()