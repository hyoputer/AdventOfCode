import intcom

def make_map(output):
  m = [['.' for i in range(60)] for i in range(40)]
  y = 1
  x = 1
  for e in output:
      m[y][x] = e
      x += 1
      if e == '\n':
        y += 1
        x = 1
  return m

def part1(m):
  res = 0
  
  for i, e1 in enumerate(m):
    for j, e2 in enumerate(e1):
      if e2 == '#' and m[i-1][j] == '#' and m[i-1][j-1] == '#' and m[i-1][j+1] == '#' and m[i-2][j] == '#':
        res += ((i-2) * (j-1))
      
#  for e1 in m:
 #   for e2 in e1:
  #    print(e2,end='')
      
  return res
  
def next_step(cur, curd, turn):
  d = [[-1,0],[0,1],[1,0],[0,-1]]
  
  if turn == 'l':
    curd -= 1
  elif turn == 'r':
    curd += 1
  elif turn == '0':
    pass
  else:
    print('error')
  
  return [cur[0] + d[curd%4][0], cur[1] + d[curd%4][1]]

def make_input(string):
  res = []
  
  for i, c in enumerate(string):
    res.append(ord(c))
    if c.isalpha():
      res.append(ord(','))
    elif i+1 < len(string) and c.isdigit() and string[i+1].isalpha():
      res.append(ord(','))
    elif i+1 == len(string):
      res.append(ord(','))
    
  res[-1] = ord('\n')
  #print(res)
  return res
  
def part2(com, m):
  d = [[-1,0],[0,1],[1,0],[0,-1]]
  curd = 0
  
  for i, e1 in enumerate(m):
    for j, e2 in enumerate(e1):
      if e2 == '^':
        start = [i,j]
  
  res = []
  cur = start
  while True:
    nstep = next_step(cur, curd, '0')
    if m[nstep[0]][nstep[1]] != '#':
      lstep = next_step(cur, curd, 'l')
      rstep = next_step(cur, curd, 'r')
      if m[lstep[0]][lstep[1]] == '#':
        curd -= 1
        res.append('L')
        continue
      elif m[rstep[0]][rstep[1]] == '#':
        curd += 1
        res.append('R')
        continue
      else:
        break
    else:
      if res[-1] == 'L' or res[-1] == 'R':
        res.append(1)
      else:
        res[-1] += 1
        
      cur = nstep
      
  print (res)
  
  com.put_Input(make_input('ABACBCBCAC'))
  com.put_Input(make_input('L10R12R12'))
  com.put_Input(make_input('R6R10L10'))
  com.put_Input(make_input('R10L10L12R6'))
  com.put_Input(make_input('n'))
  
  com.run()
  
  return com.get_Last_Output()

inline = input()

code_str = inline.split(',')

code = list(map(int, code_str))

com = intcom.intcomProgram(code[:])
com.run()

o = com.get_Output()
ASCII_OUTPUT = [chr(e) for e in list(o.queue)]
m = make_map(ASCII_OUTPUT)

print(''.join(ASCII_OUTPUT))
print(part1(m))

code[0] = 2

print('com2')
com2 = intcom.intcomProgram(code[:])

print(part2(com2, m))