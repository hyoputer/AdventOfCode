import intcom

def make_input(string):
  res = []
  for c in string:
    res.append(ord(c))
    
  res.append(10)
  
  return res

def parse_input():
  
  inline = input()

  code_str = inline.split(',')

  code = list(map(int, code_str))
  
  return code

def part1():
  code = parse_input()
  
  com = intcom.intcomProgram(code)
  com.put_Input(make_input('NOT A J'))
  com.put_Input(make_input('NOT B T'))
  com.put_Input(make_input('OR T J'))
  com.put_Input(make_input('NOT C T'))
  com.put_Input(make_input('OR T J'))
  com.put_Input(make_input('AND D J'))
  com.put_Input(make_input('WALK'))
  
  com.run()
  
  #o = com.get_Output()
  
  #print(''.join(list(map(lambda x : chr(x), list(o.queue) ))))
  return com.get_Last_Output()
  
def part2():
  code = parse_input()
  
  com = intcom.intcomProgram(code)
  com.put_Input(make_input('NOT A T'))
  com.put_Input(make_input('OR T J'))
  com.put_Input(make_input('NOT B T'))
  com.put_Input(make_input('OR T J'))
  com.put_Input(make_input('NOT C T'))
  com.put_Input(make_input('OR T J'))
  com.put_Input(make_input('AND D J'))
  com.put_Input(make_input('NOT E T'))
  com.put_Input(make_input('AND H T'))
  com.put_Input(make_input('OR E T'))
  com.put_Input(make_input('AND T J'))
  com.put_Input(make_input('RUN'))
  
  com.run()
  
  #o = com.get_Output()
  
  #print(''.join(list(map(lambda x : chr(x), list(o.queue) ))))
  return com.get_Last_Output()
  
  
#print(part1())
print(part2())