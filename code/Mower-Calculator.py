blen = int(input('Enter block length: '))
bwid = int(input('Enter block width: '))
hlen = int(input('Enter house length: '))
hwid  = int(input('Enter house width: '))

barea = blen * bwid
harea = hlen * hwid

price = ((barea * 35) - (harea * 35))
print('Mowing cost is ' + str(price) + ' baht.')
