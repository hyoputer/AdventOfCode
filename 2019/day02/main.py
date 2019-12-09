inline = input()

code_str = inline.split(',')

code = list(map(int, code_str))

code[1] = 72
code[2] = 64

idx = 0

while idx < len(code):
  if code[idx] == 1:
    a = code[code[idx+1]]
    b = code[code[idx+2]]
    code[code[idx+3]] = a+b
  elif code[idx] == 2:
    a = code[code[idx+1]]
    b = code[code[idx+2]]
    code[code[idx+3]] = a*b
  elif code[idx] == 99:
    print(code[0])
    break
  else:
    print('error')
    
  idx+=4