fn = 'input_06_test.txt'
#fn = 'input_06.txt'

data = [int(x) for x in (open(fn).readline()).split(',')]
data = [3]
def procreate(arr,n):
  if n == 0: return
  else:
    for i in range(len(arr)):
      if arr[i] == 0:
        arr[i] = 6
        arr.append(8)
      else:
        arr[i] -= 1 
    procreate(arr,n-1)
  return len(arr)

tot = sum([procreate([d],80) for d in data])
print('Part 1: ',tot)

# tot = sum([procreate([d],265) for d in data])
# print('Part 1: ',tot)


