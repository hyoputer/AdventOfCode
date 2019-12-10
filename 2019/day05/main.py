import intcom

inline = input()

code_str = inline.split(',')

code = list(map(int, code_str))

com = intcom.intcomProgram(code)

com.put_input([5])

com.run()

while not com.if_done():
  pass

output = com.get_output()


while True:
  print(output.get(block=False))