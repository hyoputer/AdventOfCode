import intcom

inline = input()

code_str = inline.split(',')

code = list(map(int, code_str))

com = intcom.intcomProgram(code)

com.put_Input([2])

com.run()

output = com.get_Output()

while not output.empty():
  print(output.get(block=False))