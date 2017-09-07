n = 5
count = 0
total = 0
startCount = n - 3

while True:
  
  if count == n:
    break
  
  elif count < n:
    x = int(input())
    
    if count > startCount:
      total = total + x
      
  count = count + 1

print('')
print('Sum is %d.' % total)
