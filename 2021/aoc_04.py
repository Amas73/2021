fn = 'input_04_test.txt'
fn = 'input_04.txt'

def check_board(lst_boards):
  for c in calls:
    t_boards = []
    for i in range(len(lst_boards)):
      t_board = [[itm for itm in r if itm != c] for r in lst_boards[i]]
      t_boards.append(t_board)
      if [] in t_board: break
    lst_boards = t_boards[:]
    if [] in t_board: break
  brd_sum = sum([sum(a) for a in t_board])
  return [calls.index(c),c,brd_sum]


data = [r.strip('\n') for r in open(fn).readlines()]
calls = [int(i) for i in data[0].split(',')]

boards=[]
tmp_brd = []
for i in data[2:]:
  if i == '':
    boards.append(tmp_brd)
    tmp_brd = []
  else: tmp_brd.append([int(a) for a in i.replace('  ',' ').strip().split(' ')])
boards.append(tmp_brd)

h_boards = boards[:]
v_boards = []
for i in range(len(boards)):
  t_board = []
  for x in range(len(boards[i][0])):
    row = []
    for r in boards[i]:
      row.append(r[x])
    t_board.append(row)
  v_boards.append(t_board)

chk = []
chk.append(check_board(v_boards))
chk.append(check_board(h_boards))
best = int(chk[0][0] > chk[1][0])
print('Part 1: ',str(chk[best][1]*chk[best][2]))


def check_allboards(lst_boards):
  tracker = [[] for a in range(len(lst_boards))]
  for c in calls:
    t_boards = []
    for b in range(len(lst_boards)):
      t_board = [[itm for itm in r if itm != c] for r in lst_boards[b]]
      t_boards.append(t_board)
      if [] in t_board and tracker[b] == []: tracker[b] = [calls.index(c),c,sum([sum(a) for a in t_board])]
    lst_boards = t_boards[:]
    if sum([int(i!=[]) for i in tracker]) == len(lst_boards): break
  return tracker

chk = []
chk.append(check_allboards(v_boards))
chk.append(check_allboards(h_boards))
mn = [[] for a in range(len(boards))]
for b in range(len(chk[0])):
  if chk[0][b] < chk[1][b]:
    mn[b] = chk[0][b]
  else:
    mn[b] = chk[1][b]
mx = [0,0,0]
for b in mn:
  if b[0] > mx[0]: mx=b

print('Part 2: ', str(mx[1]*mx[2]))