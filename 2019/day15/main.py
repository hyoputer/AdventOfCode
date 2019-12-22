import intcom
import queue

inline = input()

code_str = inline.split(',')

code = list(map(int, code_str))

def get_next_direction(m, current_position):
  d = [[0,1],[0,-1],[-1,0],[1,0]]
  curd = 0
  visited = 1e9
  
  for i in range(4):
    next_position = m[current_position[0]+d[i][0]][current_position[1]+d[i][1]]
    if next_position != -1 and next_position < visited:
      curd = i
      visited = next_position
  
  return curd

def make_map(com, m, current_position):
  d = [[0,1],[0,-1],[-1,0],[1,0]]
  status = 0
  while True:
    curd = get_next_direction(m, current_position)
    com.put_Input([curd+1])
    com.run()

    status = com.get_Last_Output()
    if status == 0:
      m[current_position[0]+d[curd][0]][current_position[1]+d[curd][1]] = -1
    elif status == 1:
      current_position[0] += d[curd][0]
      current_position[1] += d[curd][1]
      m[current_position[0]][current_position[1]] += 1
    elif status == 2:
      current_position[0] += d[curd][0]
      current_position[1] += d[curd][1]
      m[current_position[0]][current_position[1]] += 1
      break


def part1(m, current_position):
  
  #print(current_position)
  
  d = [[0,1],[0,-1],[-1,0],[1,0]]
  q = queue.Queue()
  q.put([25,25,0])
  res = 0
  
  visited = [[0 for i in range(50)] for i in range(50)]
  visited[25][25] = 1
  
  while not q.empty():
    cur = q.get()
    #print(cur)
    if cur[0] == current_position[0] and cur[1] == current_position[1]:
      res = cur
      break
    
    else:
      for i in range(4):
        nexty = cur[0]+d[i][0]
        nextx = cur[1]+d[i][1]
        if m[nexty][nextx] != -1 and m[nexty][nextx] != 0 and visited[nexty][nextx] != 1:
          #print(m[nexty][nextx])
          q.put([nexty, nextx, cur[2]+1])
          visited[nexty][nextx] = 1
  
  return res

def part2(m, current_position):
  
  #print(current_position)
  
  d = [[0,1],[0,-1],[-1,0],[1,0]]
  q = queue.Queue()
  q.put([current_position[0],current_position[1],0])
  res = 0
  
  visited = [[0 for i in range(50)] for i in range(50)]
  visited[current_position[0]][current_position[1]] = 1
  
  while not q.empty():
    cur = q.get()
    res = cur[2]
    
    for i in range(4):
      nexty = cur[0]+d[i][0]
      nextx = cur[1]+d[i][1]
      if m[nexty][nextx] != -1 and m[nexty][nextx] != 0 and visited[nexty][nextx] != 1:
        #print(m[nexty][nextx])
        q.put([nexty, nextx, cur[2]+1])
        visited[nexty][nextx] = 1
  
  return res
  


com = intcom.intcomProgram(code)

m = [[0 for i in range(50)] for i in range(50)]
current_position = [25,25]
m[25][25] = 1

make_map(com, m, current_position)
  
ox_droid = part1(m, current_position)

print(ox_droid[2])
print(part2(m, ox_droid[:2]))