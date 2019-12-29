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
    return str(self.current) + " [" + bin(self.collected_keys) + "] :" + str(self.length)

def get_grid():
  grid = collections.defaultdict(int)

  keys = {}
  doors = {}

  for y, line in enumerate(sys.stdin):
    for x, e in enumerate(line):
      if e != '#':
        p = Point(x, y)
        grid[p] = 1
        if e == '@':
          start_point = p
        elif e != '.':
          if ord(e) >= 97:
            keys[ord(e)-97] = p
          else:
            doors[ord(e)-65] = p
            
  return grid, keys, doors, start_point, x, y

def surrounding_points(p):
  return [
    Point(p.x, p.y-1),
    Point(p.x, p.y+1),
    Point(p.x+1, p.y),
    Point(p.x-1, p.y)
  ]

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
  
  for k, p in doors.items():
    if p in path:
      doors_in_way[k] = 1
  distance = len(path) - 1
  return distance, doors_in_way

def get_key_to_key(G, start_point, keys, doors):
  key_to_key = collections.defaultdict(dict)
  for k, p in keys.items():
    res = get_distance(G, start_point, p, doors)
    if res is not None:
      distance, doors_in_way = res
      key_to_key[-1][k] = (distance, doors_in_way)
      
  for k0, k1 in itertools.combinations(keys.keys(), 2):
    res = get_distance(G, keys[k0], keys[k1], doors)
    if res is not None:
      distance, doors_in_way = res
      key_to_key[k0][k1] = (distance, doors_in_way)
      key_to_key[k1][k0] = (distance, doors_in_way)
    
  return key_to_key

def if_have_all_keys(collected_keys, doors_in_way):
  for d in doors_in_way.keys():
    if not (1 << d) & collected_keys:
      return False
  
  return True

def find_next_possible_path(key_to_key, path):
  current_position = path.current
  for k, v in key_to_key[current_position].items():
    distance, doors_in_way = v
    if not (1 << k) & path.collected_keys:
      if if_have_all_keys(path.collected_keys, doors_in_way):
        yield Path(k, path.collected_keys + (1<<k), path.length + distance)

def part1():
  grid, keys, doors, start_point, max_x, max_y = get_grid()
  
  G = build_graph(grid, max_x, max_y)
  key_to_key = get_key_to_key(G, start_point, keys, doors)
  
  total_keys = len(keys)
  
  q = queue.Queue()
  q.put(Path(-1, 0, 0))
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
        if new_path.key_counts() == total_keys:
          if new_path.length < min_full_path_length:
            min_full_path_length = new_path.length
        else:
          q.put(new_path)
          
  return min_full_path_length

print(part1())