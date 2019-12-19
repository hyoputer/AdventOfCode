import intcom

inline = input()

code_str = inline.split(',')

code = list(map(int, code_str))

com = intcom.intcomProgram(code)

com.run()

o = com.get_Output()

t = list(o.queue)

print([e for i, e in enumerate(t) if i%3 == 2].count(2))

