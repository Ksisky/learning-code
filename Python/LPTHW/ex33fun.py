def makelist(a):
	i = 0
	numbers = []
	stopnum = int(raw_input('> ')) + 1
	while i < stopnum:
		print "At the top of i is %d" % i
		numbers.append(i)
		
		i = i + a
		print "Numbers now: ", numbers
		if i != 6:
			print "At the bottom of i is %d" % i


	print "The numbers: "

	for num in numbers:
		print num