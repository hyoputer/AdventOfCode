import intcom

inline = input()

code_str = inline.split(',')

code = list(map(int, code_str))
code[0] = 2

com = intcom.intcomProgram(code)

res = 0
while not com.is_done():
  com.run()
  
  ball_p = 0
  paddle_p = 0
  
  o = com.get_Output()
  t = list(o.queue)
  
  idx = 0
  while True:
    if idx+2 >= len(t):
      break
    if t[idx] == -1 and t[idx+1] == 0:
      res = t[idx+2]
    if t[idx+2] == 3:
      paddle_p = t[idx] 
    elif t[idx+2] == 4:
      ball_p = t[idx]
    idx += 3
    
  com.put_Input([(ball_p > paddle_p) - (paddle_p > ball_p)])
  
print(res)