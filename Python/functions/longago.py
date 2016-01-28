import time
def timesince(tuple):
	import time
	ctime = time.time() #Returns current time as SSE
	ttime = time.gmtime() #Returns current time as tuple.
	ptime = time.mktime(tuple) #Turns the past time into a SSE
	dtime = ctime - ptime #SSE Difference in time.
	year1 = int(time.strftime("%Y", ttime))
	year2 = int(time.strftime("%Y", tuple))
	yeard = year1 - year2
	