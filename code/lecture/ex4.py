m = int(input('Enter m: '))
n = int(input('Enter n: '))

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

getCount = count
count = 0
counter = 0
newStorage = {}

while count < getCount:
  
  if storage[count] >= m and storage[count] <= n:
    newStorage[counter % 2] = storage[count]
    counter += 1

  count += 1  

total = newStorage[0] + newStorage[1]
print('Sum is %d' %total)
