fn = 'input_02_test.txt'
fn = 'input_02.txt'

data = [[a,int(b)] for a,b in [r.split(' ') for r in open(fn).readlines()]]

hp,d = 0,0
for cmd,adj in data:
  if cmd == 'forward': hp+=adj
  elif cmd == 'up': d-=adj
  elif cmd == 'down': d+=adj

print('Part a:', str(hp*d))

hp,d, aim = 0,0,0
for cmd,adj in data:
  if cmd == 'forward': 
    hp+=adj
    d+=adj*aim
  elif cmd == 'up': aim-=adj
  elif cmd == 'down': aim+=adj

print('Part b:', str(hp*d))