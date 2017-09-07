count = 0
total = 0
startCount = 0
storage = {}


while True:
  
  x = int(input())
  
  if x == 0:
    if count < 2:
      print('error')
    break
  
  storage[count] = x
  count += 1

startCount = count - 2
total = storage[startCount] + storage[startCount + 1]
print('Sum is %d' %total)
