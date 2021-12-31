fn = 'input_03_test.txt'
fn = 'input_03.txt'

data = [r.strip('\n').split(' ')[0] for r in open(fn).readlines()]

g=[0 for i in range(len(data[0]))]
for r in data:
  for x,v in enumerate(r):
    if v=='1': g[x]+=1

gamma = ''
epsilon = ''
for x in g:
  result=(x>(len(data)/2))
  gamma+=str(int(result))
  epsilon+=str(int(not(result)))

print('Part a:', str((int(gamma,2)*int(epsilon,2))))

o=data[:]
c=data[:]
def process_list(lst,pos,chk_bit):
  cnt=0
  s=''
  rows=len(lst)
  for r in lst:
    cnt+=int(r[pos]=='1')
  result=str(int((chk_bit=='1') == (cnt>=rows/2)))
  for r in range(rows-1,-1,-1):
    if lst[r][pos]!=result:
      lst.pop(r)
  if len(lst)==1 or pos==len(lst[0])-1: return lst[0]
  else: process_list(lst,pos+1,chk_bit)
  return lst[0]

oxygen = int(process_list(o,0,'1'),2)
carbon = int(process_list(c,0,'0'),2)
print('Part b:', str(oxygen*carbon))
