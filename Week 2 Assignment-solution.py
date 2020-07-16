import re
hand = open('realdata.txt')
numlist = list()
for line in hand:
	stuff = sum(re.findall('[0-9]+',line))
	numlist = numlist + stuff
sum=0
for z in numlist:
    sum = sum + int(z)
print(sum)
