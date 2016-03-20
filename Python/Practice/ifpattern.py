heading = int(raw_input('What is the runway heading? > '))
pattern = raw_input('Left or Right Pattern? > ')
ubaser = heading + 90
if ubaser > 360:
	ubaser -= 360
ubasel = heading - 90
if ubasel < 0:
	ubasel += 360
downwind = heading + 180
if downwind > 360:
	downwind-= 360
basel = downwind - 90
if basel < 0:
	basel += 360
baser = downwind + 90
if baser > 360:
	baser -= 360

if pattern == 'left':
	print "Upwind Base:", ubasel,"\nDownwind:", downwind,"\nBase:", basel
if pattern == 'right':
	print "Upwind Base:", ubaser,"\nDownwind:", downwind,"\nBase:", baser
	
