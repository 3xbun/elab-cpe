count = 0
total = 0
startCount = 0
storage = {}

while True:
  
  x = int(input())
  check = input('Next value (y/n)? ')
  
  storage[count] = x
  count += 1  
  
  if check == 'n':
    break
  
startCount = count - 2
total = storage[startCount] + storage[startCount + 1]
print('Sum is %d' %total)
