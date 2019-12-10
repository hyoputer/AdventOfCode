import intcom
import itertools

inline = input()

code_str = inline.split(',')

code = list(map(int, code_str))

coms = [0,0,0,0,0]

perms = itertools.permutations(range(5,10))

res = 0

for p in perms:

  for i in range(5):
    coms[i] = intcom.intcomProgram(code)
    coms[i].put_Input([p[i]])
    
  coms[0].put_Input([0])
  
  while not coms[4].is_done():
    for i in range(5):
      coms[i].run()
      coms[(i+1)%5].put_Input([coms[i].get_Last_Output()])
      
  res = max(res, coms[4].get_Last_Output())
  #print(p)
  #print(coms[4].get_Last_Output())
  
print(res)