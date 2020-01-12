import intcom
import itertools

def parse_input():
  
  inline = input()

  code_str = inline.split(',')

  code = list(map(int, code_str))
  
  return code

def to_ascii(string):
  res = []
  for c in string:
    res.append(ord(c))
    
  res.append(10)
  
  return res

def to_string(li):
  res = ''
  for e in li:
    res += chr(e)
    
  return res


def part1():
  code = parse_input()
  com = intcom.intcomProgram(code[:])
  
  inventory = ['sand', 'space heater', 'loom', 'wreath', 'space law space brochure', 'pointer', 'planetoid', 'festive hat']
  
  com.put_Input(to_ascii('north')+to_ascii('north')+to_ascii('take sand')+to_ascii('south')+to_ascii('south')+to_ascii('south')+to_ascii('take space heater')+
                to_ascii('south')+to_ascii('east')+to_ascii('take loom')+to_ascii('west')+to_ascii('north')+to_ascii('west')+to_ascii('take wreath')+to_ascii('south')+
               to_ascii('take space law space brochure')+to_ascii('south')+to_ascii('take pointer')+to_ascii('north')+to_ascii('north')+to_ascii('east')+to_ascii('north')+
               to_ascii('west')+to_ascii('south')+to_ascii('take planetoid')+to_ascii('north')+to_ascii('west')+to_ascii('take festive hat')+to_ascii('south')+to_ascii('west')+
               to_ascii('inv'))
  
  for i in range(8+1):
    for combinations in itertools.combinations(inventory, i):
      for e in combinations:
        com.put_Input(to_ascii('drop '+e))
        
      com.put_Input(to_ascii('north'))
      com.run()

      o = com.get_Output()
      print(to_string(list(o.queue)))
      
      for e in combinations:
        com.put_Input(to_ascii('take '+e))
  
  
part1()