def timesince(tuple):
	import time
	ctime = time.time() #Returns current time as SSE
	ptime = time.mktime(tuple) #Turns the past time into a SSE
	dtime = ctime - ptime #Difference in time.