import collections
import queue
import math
import sys

def make_ingredient(string):
  p = string.split(' ')
  return {'ingredient': p[1].rstrip(), 'amount': int(p[0])}

def make_recepies(data):
  recepies = {}
  for line in data:
    input_str, output_str = line.split(' => ')

    ingredients = []
    for ingredient in input_str.split(', '):
      ingredients.append(make_ingredient(ingredient))

    output = make_ingredient(output_str)

    recepies[output['ingredient']] = {
      'servings': output['amount'],
      'ingredients': ingredients
    }
    
  return recepies

def get_fuel(recepies, amount):
  orders = queue.Queue()
  supply = collections.defaultdict(int)
  res = 0
  orders.put({'ingredient': 'FUEL', 'amount': amount})

  while not orders.empty():
    order = orders.get()
    if order['ingredient'] == 'ORE':
      res += order['amount']
    elif order['amount'] <= supply[order['ingredient']]:
      supply[order['ingredient']] -= order['amount']

    else:
      cur = recepies[order['ingredient']]
      order['amount'] -= supply[order['ingredient']]
      batches = math.ceil(order['amount'] / cur['servings'])
      for ingredient in cur['ingredients']:
        orders.put({'ingredient': ingredient['ingredient'], 'amount': batches * ingredient['amount']})
      leftover = batches * cur['servings'] - order['amount']
      supply[order['ingredient']] = leftover

  return res

def part1(recepies):
  return get_fuel(recepies, 1)

def part2(recepies):
  upper_bound = None
  lower_bound = 1
  ore_capacity = 1000000000000
  
  while lower_bound + 1 != upper_bound:
    if upper_bound == None:
      guess = lower_bound * 2
    else:
      guess = (lower_bound + upper_bound) // 2
      
    ore_needed = get_fuel(recepies, guess)
    
    if ore_needed > ore_capacity:
      upper_bound = guess
    else:
      lower_bound = guess
      
  return lower_bound
  
data = []

for line in sys.stdin:
  data.append(line)


recepies = make_recepies(data)




print(part1(recepies))
print(part2(recepies))