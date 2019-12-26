import intcom

def make_map(output):
  m = [[0 for i in range(56)] for i in range(36)]
  y = 0
  x = 0
  for e in output:
      m[y][x] = e
      x += 1
      if e == '\n':
        y += 1
        x = 0
  return m

def part1(output):
  m = [[0 for i in range(56)] for i in range(36)]
  y = 0
  x = 0
  res = 0
  for e in output:
    m[y][x] = e
    if y >= 2 and x > 0 and e == '#' and m[y-1][x] == '#' and m[y-1][x-1] == '#' and m[y-1][x+1] == '#' and m[y-2][x] == '#':
      res += ((y-1) * x)
      #print(y-1)
      #print(x)
    x += 1
    if e == '\n':
      y += 1
      x = 0
      
#  for e1 in m:
 #   for e2 in e1:
  #    print(e2,end='')
      
  print(res)
  
def part2(com, output):
  d = [[-1,0],[0,1],[1,0],[0,-1]]
  curd = 0

inline = input()

code_str = inline.split(',')

code = list(map(int, code_str))

com = intcom.intcomProgram(code)

com.run()

o = com.get_Output()
ASCII_OUTPUT = [chr(e) for e in list(o.queue)]


print(''.join(ASCII_OUTPUT))
part1(ASCII_OUTPUT)

code[0] = 2
com2 = intcom.intcomProgram(code)

part2(com2, ASCII_OUTPUT)