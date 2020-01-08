import collections
import networkx as nx
import sys
import queue
import itertools

Point = collections.namedtuple('P', 'x y')

class Path():
  def __init__(self, current, layer, length):
    self.current = current
    self.layer = layer
    self.length = length
    
  def get_state(self):
    return (self.current, self.layer)
    
  def __repr__(self):
    return self.current+' '+str(self.layer)+' '+str(self.length)

def get_surrounding_points(p):
  return [
    Point(p.x+1, p.y),
    Point(p.x-1, p.y),
    Point(p.x, p.y+1),
    Point(p.x, p.y-1)
  ]

def get_portal(lines, p):
  for i, sp in enumerate(get_surrounding_points(p)):
    if ord(lines[sp.y][sp.x]) >= 65:
      if i == 0:
        return ''.join(lines[p.y][p.x+1:p.x+3])
      elif i == 1:
        return ''.join(lines[p.y][p.x-2:p.x])
      elif i == 2:
        return lines[p.y+1][p.x]+lines[p.y+2][p.x]
      elif i == 3:
        return lines[p.y-2][p.x]+lines[p.y-1][p.x]
      
  return None

def get_grid():
  grid = collections.defaultdict(int)
  portals = collections.defaultdict(list)
  
  lines = list(map(lambda line : list(line.rstrip()), sys.stdin))
  #print(lines)
  max_x = 0
  for y, line in enumerate(lines):
    for x, e in enumerate(line):
      if e == '.':
        p = Point(x, y)
        grid[p] = 1
        portal_name = get_portal(lines, p)
        if portal_name is not None:
          portals[portal_name].append(p)
      max_x = max(x, max_x)
      
  for pn in portals:
    portals[pn] = sorted(portals[pn], key=lambda p: -((p.x-max_x/2)*(p.x-max_x/2) + (p.y-y/2)*(p.y-y/2)))
  #  if len(portals[pn]) == 2:
   #   print(portals[pn][0], portals[pn][1])
      
  return grid, portals, max_x, y

def build_graph(grid, portals, max_x, max_y, part1=True):
  edges = []
  for y in range(max_y+1):
    for x in range(max_x+1):
      p = Point(x, y)
      if grid[p]:
        for sp in get_surrounding_points(p):
          if grid[sp]:
            edges.append((p, sp))
            
          
  if part1:
    for portal_name in portals:
      current_portal = portals[portal_name]
      if len(current_portal) == 2:
        edges.append((current_portal[0], current_portal[1]))
      
  return nx.Graph(edges), portals['AA'][0], portals['ZZ'][0]

def get_distance(G, p0, p1):
  if not nx.has_path(G, p0, p1):
    return None
  else:
    return len(nx.shortest_path(G, p0, p1)) - 1

def get_portal_to_portal(G, portals):
  portal_to_portal = collections.defaultdict(list)
  
  for p0s, p1s in itertools.combinations(portals.keys(), 2):
    for i, p0 in enumerate(portals[p0s]):
      new_portal0_name = p0s+str(i)
      for j, p1 in enumerate(portals[p1s]):
        new_portal1_name = p1s+str(j)
        length = get_distance(G, p0, p1)
        if length is not None:
          portal_to_portal[new_portal0_name].append((new_portal1_name, length))
          portal_to_portal[new_portal1_name].append((new_portal0_name, length))
          
  #print(portal_to_portal['AA0'])
  return portal_to_portal

def get_next_path(path, portal_to_portal):
  for np in portal_to_portal[path.current]:
    if path.layer == 0:
      if np[0] == 'ZZ0':
        yield Path(np[0], path.layer, path.length+np[1])
      elif np[0][2] == '0':
        continue
      else:
        yield Path(np[0][:2]+'0', path.layer+1, path.length+np[1]+1)
    else:
      if np[0] == 'ZZ0' or np[0] == 'AA0':
        continue
      elif np[0][2] == '0':
        yield Path(np[0][:2]+'1', path.layer-1, path.length+np[1]+1)
      elif np[0][2] == '1':
        yield Path(np[0][:2]+'0', path.layer+1, path.length+np[1]+1)
      else:
        print('error')
  
def part1():
  grid, portals, max_x, max_y = get_grid()
  G, start_point, goal = build_graph(grid, portals, max_x, max_y)
  return len(nx.shortest_path(G, start_point, goal))-1

def part2():
  grid, portals, max_x, max_y = get_grid()
  G, start_point, goal = build_graph(grid, portals, max_x, max_y, False)
  portal_to_portal = get_portal_to_portal(G, portals)
  
  q = queue.Queue()
  start_path = Path('AA0', 0, 0)
  q.put(start_path)
  min_full_path_length = 1e9
  min_path_length = collections.defaultdict(int)
  portal_layers = collections.defaultdict(int)
  
  while min_full_path_length == 1e9:
    path = q.get()
    #print('----------------------')
    #print(path.__repr__())
    #print('-----------------------')
    
    if  min_path_length[path.get_state()] < path.length:
      #print(path.__repr__())
      continue
      
    for new_path in get_next_path(path, portal_to_portal):
      #print(new_path.__repr__())
      if new_path.length < min_full_path_length:
        new_state = new_path.get_state()
        better_path = False
        if new_path.length < min_path_length[new_state]:
          min_path_length[new_state] = new_path.length
          better_path = True
        else:
          min_path_length[new_state] = new_path.length
          better_path = True
      else:
        min_path_length[new_path.get_state()] = new_path.length
        better_path = True
          
      if better_path:
        if new_path.current == 'ZZ0':
          min_full_path_length = min(new_path.length, min_full_path_length)
        else:
          q.put(new_path)
          
  print(min_full_path_length)

#print(part1())
part2()