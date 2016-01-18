#For those reading this on GitHub, I have provided
#ex16-example.txt for use as the target file.
from sys import argv #Imports sys.argv

script, filename = argv #sets arguments
#Prints some stuff
print("We're going to erase %r." % filename) 
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

raw_input("?") #Asks for conformation input.
#opens file.
print("Opening the file...")
target = open(filename, 'w')
#deletes file
print "Truncating the file. Goodbye!"
target.truncate()

print("Now I'm going to ask you for 3 lines.")
#asks for input
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print("I'm going to write these to the file.")
#writes in file
target.write("%s\n%s\n%s\n" % (line1, line2, line3))
#closes file
print("And finally, we close it.")
target.close()