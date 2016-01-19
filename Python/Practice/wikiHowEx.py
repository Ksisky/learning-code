from time import asctime, mktime, time
#3-5 prints current time as tuple
print("The current time is:"),
current_time = asctime()
print(current_time)

current_sse = time()
foundedt = 2005, 1, 15, 0, 0, 0, 5, 15, -1 #Struct time of wikiHows founding.
founded = mktime(foundedt)#SSE of wikiHows founding
difference = current_sse - founded

years = difference / 31557600
years = round(years, 0)
years = int(years)
print(years)

months = difference % 31557600

#print("wikiHow was founded on January 15, 2005, which was %d years, %d months, and %d days ago." % (years, months, days))
