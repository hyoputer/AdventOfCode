import sys

def get_initial_map():
  m = []
  for line in sys.stdin:
    m.append(list(line.rstrip()))
    
  return m

def get_adjacent_tiles(m, x, y):
  res = []
  
  if x > 0:
    res.append(m[y][x-1])
  
  if y > 0:
    res.append(m[y-1][x])
    
  if x < len(m) - 1:
    res.append(m[y][x+1])
    
  if y < len(m) - 1:
    res.append(m[y+1][x])
    
  return res

def get_adjacent_bugs(m, x, y):
  res = 0
  for e in get_adjacent_tiles(m, x, y):
    if e == '#':
      res += 1
      
  return res

def get_next_map(m):
  new_map = [[0 for i in range(len(m))] for i in range(len(m))]
  for y, line in enumerate(m):
    for x, e in enumerate(line):
      if e == '#' and not get_adjacent_bugs(m, x, y) == 1:
        new_map[y][x] = '.'
        continue
      elif e == '.':
        adjacent_bugs = get_adjacent_bugs(m, x, y)
        if adjacent_bugs == 1 or adjacent_bugs == 2:
          new_map[y][x] = '#'
          continue
          
      new_map[y][x] = m[y][x]
      
  return new_map
          
def get_biodiversity_rating(m):
  res = 0
  for y, line in enumerate(m):
    for x, e in enumerate(line):
      if e == '#':
        res += 2 ** (x + 5 * y)
      
  return res

def blank_map(size):
  new_map =  [['.' for i in range(size)] for i in range(size)]
  new_map[2][2] = '?'
  return new_map

def get_adjacent_tiles_part2(map_layers, x, y, k):
  res = []
  
  map_size = len(map_layers[0])
  layer_size = len(map_layers)
  
  if x == 0 and k > 0:
    res.append(map_layers[k-1][2][1])
  elif x == 3 and y == 2 and k < layer_size - 1:
    for i in range(map_size):
      res.append(map_layers[k+1][i][4])
  elif x > 0:
    res.append(map_layers[k][y][x-1])
  
  if y == 0 and k > 0:
    res.append(map_layers[k-1][1][2])
  elif x == 2 and y == 3 and k < layer_size - 1:
    for i in range(map_size):
      res.append(map_layers[k+1][4][i])
  elif y > 0:
    res.append(map_layers[k][y-1][x])
    
  if x == map_size - 1 and k > 0:
    res.append(map_layers[k-1][2][3])
  elif x == 1 and y == 2 and k < layer_size - 1:
    for i in range(map_size):
      res.append(map_layers[k+1][i][0])
  elif x < map_size - 1:
    res.append(map_layers[k][y][x+1])
    
  if y == map_size - 1 and k > 0:
    res.append(map_layers[k-1][3][2])
  elif x == 2 and y == 1 and k < layer_size - 1:
    for i in range(map_size):
      res.append(map_layers[k+1][0][i])
  elif y < map_size - 1:
    res.append(map_layers[k][y+1][x])
    
  return res
  

def get_adjacent_bugs_part2(map_layers, x, y, k):
  res = 0
  for e in get_adjacent_tiles_part2(map_layers, x, y, k):
    if e == '#':
      res += 1
      
  return res

def get_next_map_layers(map_layers, even_flag):
  if even_flag:
    map_layers.insert(0, blank_map(len(map_layers[0])))
    map_layers.append(blank_map(len(map_layers[0])))
    
  new_map_layers = [[[0 for i in range(len(map_layers[0]))] for i in range(len(map_layers[0]))] for i in range(len(map_layers))]
  
  for k, layer in enumerate(map_layers):
    for y, line in enumerate(layer):
      for x, e in enumerate(line):
        if e == '#' and not get_adjacent_bugs_part2(map_layers, x, y, k) == 1:
          new_map_layers[k][y][x] = '.'
          continue
        elif e == '.':
          adjacent_bugs = get_adjacent_bugs_part2(map_layers, x, y, k)
          if adjacent_bugs == 1 or adjacent_bugs == 2:
            new_map_layers[k][y][x] = '#'
            continue
            
        new_map_layers[k][y][x] = map_layers[k][y][x]
        
  return new_map_layers

def get_total_bugs(map_layers):
  res = 0
  for k, layer in enumerate(map_layers):
    for y, line in enumerate(layer):
      for x, e in enumerate(line):
        if e == '#':
          res += 1
          
  return res

def part1():
  current_map = get_initial_map()
  previous_biodiversity_ratings = []
  previous_biodiversity_ratings.append(get_biodiversity_rating(current_map))
  while True:
    next_map = get_next_map(current_map)
    current_biodiversity_rating = get_biodiversity_rating(next_map)
    if current_biodiversity_rating in previous_biodiversity_ratings:
      return current_biodiversity_rating
    else:
      previous_biodiversity_ratings.append(current_biodiversity_rating)
      
    current_map = next_map
    
def part2(end_time):
  map_layers = []
  initial_map = get_initial_map()
  initial_map[2][2] = '?'
  map_layers.append(initial_map)
  
  for i in range(end_time):
    even_flag = (i%2==0)
    map_layers = get_next_map_layers(map_layers, even_flag)
    
    
  total_bugs = get_total_bugs(map_layers)
    
  return total_bugs
    
#print(part1())
print(part2(200))