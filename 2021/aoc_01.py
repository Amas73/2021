fn = open('input_01_test.txt','r')
fn = open('input_01.txt','r')

def deeper(a,b,t):
  b=a
  c = fn.readline()
  if not c:
    return t-1
  else: a = int(c)
  if a > b: t+=1
  return deeper(a,b,t)

#print(deeper(0,0,0))

a,b,t=0,0,-1
while True:
  b=a
  c=fn.readline()
  if not c: break
  a=int(c)
  if a>b: t+=1

print ('Part a:',t)

fn.seek(0)
a,b,c,d,e,t=0,0,0,0,0,-3
while True:
  a=b
  b=c
  d=e
  r=fn.readline()
  if not r: break
  c=int(r)
  e=a+b+c
  if e>d: t+=1

print ('Part b:',t)