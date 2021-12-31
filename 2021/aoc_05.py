fn = 'input_05_test.txt'
fn = 'input_05.txt'

data = [l.split(' -> ') for l in [r.strip('\n') for r in open(fn).readlines()]]
coords = []
x_max,y_max = 0,0
for a in data:
  coord = []
  for b in a:
    xy=[int(c) for c in b.split(',')]
    coord.append(xy)
    x_max = max(x_max,xy[0])
    y_max = max(y_max,xy[1])
  coords.append(coord)

def populate_grid(part=1):
    grd = [[0 for i in range(x_max+1)] for a in range(y_max+1)]
    for ln in coords:
      x1,y1 = ln[0][0], ln[0][1]
      x2,y2 = ln[1][0], ln[1][1]
      x_chg = x2-x1
      y_chg = y2-y1
      if part == 1 and x_chg!=0 and y_chg!=0: pass #do nothing
      else:
        loop = max(abs(x_chg),abs(y_chg))
        if x_chg == 0: x_step = 0
        else: x_step = x_chg//abs(x_chg)
        if y_chg == 0: y_step = 0
        else: y_step = y_chg//abs(y_chg)
        for z in range(loop+1):
          grd[y1+(z*y_step)][x1+(z*x_step)] += 1
    return grd

grid = populate_grid(1)
chk = 0
for r in grid:
  chk += sum([int(i>1) for i in r])
  
print('Part 1: ',chk)

grid = populate_grid(2)
chk = 0
for r in grid:
  chk += sum([int(i>1) for i in r])
print('Part 2: ',chk)