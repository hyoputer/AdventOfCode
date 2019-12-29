import collections
import queue
import networkx as nx
import itertools
import sys

Point = collections.namedtuple('P', "x y")

class Path():
  def __init__(self, current, collected_keys, length):
    self.current = current
    self.collected_keys = collected_keys
    self.length = length
    
  def get_state(self):
    return (self.current, self.collected_keys)
  
  def key_counts(self):
    return bin(self.collected_keys).count('1')
  
  def __repr__(self):
    return bin(self.current) + " [" + bin(self.collected_keys) + "] :" + str(self.length)
  
def surrounding_points(p):
  return [
    Point(p.x, p.y-1),
    Point(p.x, p.y+1),
    Point(p.x+1, p.y),
    Point(p.x-1, p.y)
  ]

def diagonal_points(p):
  return [
    Point(p.x+1, p.y+1),
    Point(p.x+1, p.y-1),
    Point(p.x-1, p.y-1),
    Point(p.x-1, p.y+1)
  ]

def get_grid(part2=False):
  grid = collections.defaultdict(int)

  keys = {}
  doors = {}
  start_points = []

  for y, line in enumerate(sys.stdin):
    for x, e in enumerate(line.rstrip()):
      if e != '#':
        p = Point(x, y)
        grid[p] = 1
        if e == '@':
          start_points.append(p)
        elif e != '.':
          if ord(e) >= 97:
            keys[ord(e)-97] = p
          else:
            doors[ord(e)-65] = p
  if part2:
    sp = start_points[0]
    del start_points[0]
    grid[sp] = 0
    for p in surrounding_points(sp):
      grid[p] = 0
    for p in diagonal_points(sp):
      start_points.append(p)
      
  keys = {k+len(start_points) : p for k, p in keys.items()}
  doors = {d+len(start_points) : p for d, p in doors.items()}
            
  return grid, keys, doors, start_points, x, y

def build_graph(grid, max_x, max_y):
  edges = []
  for x in range(max_x+1):
    for y in range(max_y+1):
      p = Point(x, y)
      if grid[p]:
        for sp in surrounding_points(p):
          if grid[sp]:
            edges.append((p, sp))
  return nx.Graph(edges)

def get_distance(G, p0, p1, doors):
  doors_in_way = {}
  if not nx.has_path(G, p0, p1):
    return None
  path = nx.shortest_path(G, p0, p1)
  
  for d, p in doors.items():
    #print(d)
    door_to_bits = 1 << d
    if p in path:
      doors_in_way[door_to_bits] = 1
  distance = len(path) - 1
  return distance, doors_in_way

def get_key_to_key(G, start_points, keys, doors):
  key_to_key = collections.defaultdict(dict)
  for k, p in keys.items():
    key_to_bits = 1 << k
    for i, start_point in enumerate(start_points):
      res = get_distance(G, start_point, p, doors)
      start_point_bit = 1 << i
      if res is not None:
        distance, doors_in_way = res
        key_to_key[start_point_bit][key_to_bits] = (distance, doors_in_way)
      
  for k0, k1 in itertools.combinations(keys.keys(), 2):
    res = get_distance(G, keys[k0], keys[k1], doors)
    k0_to_bits = 1 << k0
    k1_to_bits = 1 << k1
    if res is not None:
      distance, doors_in_way = res
      key_to_key[k0_to_bits][k1_to_bits] = (distance, doors_in_way)
      key_to_key[k1_to_bits][k0_to_bits] = (distance, doors_in_way)
    
  return key_to_key

def if_have_all_keys(collected_keys, doors_in_way):
  for d in doors_in_way.keys():
    if not d & collected_keys:
      return False
  
  return True

def find_next_possible_path(key_to_key, path):
  current_position = path.current
  for k0, v0 in key_to_key.items():
    if k0 & current_position:
      for k1, v1 in v0.items():
        distance, doors_in_way = v1
        if not k1 & path.collected_keys:
          if if_have_all_keys(path.collected_keys, doors_in_way):
            new_position = (current_position ^ k0) | k1
            yield Path(new_position, path.collected_keys + k1, path.length + distance)

def get_shortest_path_length(grid, keys, doors, start_points, max_x, max_y):
  
  G = build_graph(grid, max_x, max_y)
  key_to_key = get_key_to_key(G, start_points, keys, doors)
  
  total_keys = len(keys)
  #print(total_keys)
  
  q = queue.Queue()
  start_point_bit = 0
  for i in range(len(start_points)):
    start_point_bit += (1<<i)
  q.put(Path(start_point_bit, 0, 0))
  min_full_path_length = 1e9
  min_path_length = collections.defaultdict(int)
  
  while not q.empty():
    path = q.get()
    if min_path_length[path.get_state()] < path.length:
      continue
    #print(path.__repr__())
    for new_path in find_next_possible_path(key_to_key, path):
      if new_path.length < min_full_path_length:
        new_state = new_path.get_state()
        better_path = False
        if new_state in min_path_length:
          if new_path.length < min_path_length[new_state]:
            better_path = True
            min_path_length[new_state] = new_path.length
        else:
          min_path_length[new_state] = new_path.length
          better_path = True
      
      if better_path:
        #print(new_path.__repr__())
        if new_path.key_counts() == total_keys:
          if new_path.length < min_full_path_length:
            min_full_path_length = new_path.length
        else:
          q.put(new_path)
          
  return min_full_path_length

def part1():
  grid, keys, doors, start_points, max_x, max_y = get_grid()
  return get_shortest_path_length(grid, keys, doors, start_points, max_x, max_y)

def part2():
  grid, keys, doors, start_points, max_x, max_y = get_grid(True)
  return get_shortest_path_length(grid, keys, doors, start_points, max_x, max_y)

#print(part1())
print(part2())