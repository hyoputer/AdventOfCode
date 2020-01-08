import sys

def part1(size):
  deck = [i for i in range(size)]
  
  for line in sys.stdin:
    current_line = line.split(' ')
    
    if current_line[0] == 'cut':
      cut_index = int(current_line[1])
      deck = deck[cut_index:] + deck[0:cut_index]
    else:
      if current_line[2] == 'increment':
        new_deck = [0 for i in range(size)]
        current_index = 0
        increment_value = int(current_line[3])
        for card in deck:
          new_deck[current_index%size] = card
          current_index += increment_value
        deck = new_deck
      else:
        deck.reverse()
        
  return deck
  
def part2(size, count, position):
  coefficient = 1
  constant = 0
  
  inputs = []
  
  for line in sys.stdin:
    inputs.append(line)
  
  for line in inputs:
    current_line = line.split(' ')

    if current_line[0] == 'cut':
      cut_index = int(current_line[1])
      constant -= cut_index
    else:
      if current_line[2] == 'increment':
        increment_value = int(current_line[3])
        coefficient *= increment_value
        constant *= increment_value
      else:
        coefficient *= -1
        constant *= -1
        constant -= 1
        
    coefficient %= size
    constant %= size
        
  old_coefficient = coefficient
  coefficient = pow(coefficient, count, size)
  
  def inv(a, mod) : return pow(a, mod-2, mod)
  
  print(coefficient)
  
  constant *= (coefficient - 1)*inv(old_coefficient-1, size)
  constant %= size
  print(constant)
  
  return ((position - constant) * inv(coefficient, size)) % size
  
#print(part1(10007).index(2019))
print(part2(119315717514047, 101741582076661, 2020))