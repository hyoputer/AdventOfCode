import intcom

def make_map(code, rng):
  m = [[0 for i in range(rng)] for i in range(rng)]
  for x in range(rng):
    for y in range(rng):
      com = intcom.intcomProgram(code[:])
      com.put_Input([x,y])
      com.run()
      m[x][y] = com.get_Last_Output()
  return m
      

def part1(code):
  m = make_map(code, 50)
  
  res = 0
  
  for line in m:
    res += line.count(1)

  return res

def part2(code):
  x = 99
  y = 0
  while True:
    f = False
    while True:
      com = intcom.intcomProgram(code[:])
      com.put_Input([x,y])
      #print([x,y])
      com.run()
      if com.get_Last_Output() == 1:
        com2 = intcom.intcomProgram(code[:])
        com2.put_Input([x-99,y+99])
        com2.run()
        if com2.get_Last_Output() == 1:
          return (x-99)*10000+y
        else:
          break
      y += 1
      
    x += 1
      

inline = input()

code_str = inline.split(',')

code = list(map(int, code_str))

  
#print(part1(code))
print(part2(code))