i = 0
numbers = []
stopnum = raw_input('> ')
while i < stopnum:
	print "At the top of i is %d" % i
	numbers.append(i)
	
	i = i + 1
	print "Numbers now: ", numbers
	print "At the bottom of i is %d" % i


print "The numbers: "

for num in numbers:
	print num