import intcom

def parse_input():
  
  inline = input()

  code_str = inline.split(',')

  code = list(map(int, code_str))
  
  return code

def problem(part2=False):
  code = parse_input()
  
  coms = []
  
  for i in range(50):
    com = intcom.intcomProgram(code[:])
    com.put_Input([i])
    com.run()
    coms.append(com)
    
  last_nat_y = 0.5
    
  while True:
    idle_flag = True
    for i in range(50):
      if coms[i].Input.empty():
        coms[i].put_Input([-1])
      else:
        idle_flag = False
        
        
      coms[i].run()
      
      output = coms[i].get_Output()
      while not output.empty():
        address = output.get()
        output_x = output.get()
        output_y = output.get()
        
        if address < 50:
          coms[address].put_Input([output_x, output_y])
          
        if address == 255:
          if not part2:
            return output_y
          else:
            NAT = [output_x, output_y]
            
        
    if idle_flag:
      if NAT[1] == last_nat_y:
        return last_nat_y
      else:
        last_nat_y = NAT[1]

      coms[0].put_Input(NAT)

  
#print(problem())
print(problem(True))
