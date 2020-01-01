import queue

class intcomProgram:
  def __init__(self, li):
    self.code = li
    self.idx = 0
    self.opcode = 0
    self.param_mode = [0, 0, 0]
    self.param_num = 0
    self.Input = queue.Queue()
    self.Output = queue.Queue()
    self.last_Output = 0
    self.next = 0
    self.rel_base = 0
    self.done = False
    
  def get_code(self):
    return self.code
    
  def run(self):
    while not self.done:
      self.parse()
      while True:
        try:
          self.operate()
        except IndexError:
          self.code.append(0)
        except Exception as e:
         # print(e)
          return False
        else:
          break
      self.idx += self.next
      
  def parse(self):
    cur = self.code[self.idx]
    self.opcode = cur % 100
    cur = int(cur/100)
    self.param_num = self.get_num_param()
    for i in range(self.param_num):
      self.param_mode[i] = cur % 10
      cur  = int(cur/10)
      
    self.next = self.param_num+1
  
  def get_num_param(self):
    if self.opcode == 1:
      return 3
    elif self.opcode == 2:
      return 3
    elif self.opcode == 3:
      return 1
    elif self.opcode == 4:
      return 1
    elif self.opcode == 5:
      return 2
    elif self.opcode == 6:
      return 2
    elif self.opcode == 7:
      return 3
    elif self.opcode == 8:
      return 3
    elif self.opcode == 9:
      return 1
    elif self.opcode == 99:
      return 0
    else:
      print('error')
    
  def operate(self):
    if self.opcode == 1:
      a = self.getV(0)
      b = self.getV(1)
      self.code[self.getA(2)] = a+b
    elif self.opcode == 2:
      a = self.getV(0)
      b = self.getV(1)
      self.code[self.getA(2)] = a*b
    elif self.opcode == 3:
      adr = self.getA(0)
      if len(self.code) <= adr:
        raise IndexError
      a = self.Input.get(block=False)
      self.code[adr] = int(a)
    elif self.opcode == 4:
      a = self.getV(0)
      self.Output.put(a, block=False)
      self.last_Output = a
    elif self.opcode == 5:
      a = self.getV(0)
      b = self.getV(1)
      if a != 0:
        self.idx = b
        self.next = 0
    elif self.opcode == 6:
      a = self.getV(0)
      b = self.getV(1)
      if a == 0:
        self.idx = b
        self.next = 0
    elif self.opcode == 7:
      a = self.getV(0)
      b = self.getV(1)
      adr = self.getA(2)
      if a < b:
        self.code[adr] = 1
      else:
        self.code[adr] = 0
    elif self.opcode == 8:
      a = self.getV(0)
      b = self.getV(1)
      adr = self.getA(2)
      if a == b:
        self.code[adr] = 1
      else:
        self.code[adr] = 0
    elif self.opcode == 9:
      a = self.getV(0)
      self.rel_base += a
    elif self.opcode == 99:
      self.done = True
      
  def getV(self, pi):
    if pi >= self.param_num:
      print('error')
      
    temp = self.code[self.idx+pi+1]

    if self.param_mode[pi] == 0:
      return self.code[temp]
    elif self.param_mode[pi] == 1:
      return temp
    elif self.param_mode[pi] == 2:
      return self.code[temp+self.rel_base]
    else:
      print('error')

  def getA(self, pi):
    if self.param_mode[pi] == 0:
      return self.code[self.idx+pi+1]
    elif self.param_mode[pi] == 2:
      return self.code[self.idx+pi+1] + self.rel_base
    else:
      print('error')

  def put_Input(self, li):
    for e in li:
      self.Input.put(e)

  def get_Output(self):
    t = self.Output
    self.Output = queue.Queue()
    return t

  def is_done(self):
    return self.done
  
  def get_Last_Output(self):
    return self.last_Output