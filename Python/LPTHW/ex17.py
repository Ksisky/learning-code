#GitHub people, I have provided ex17-test.txt and
#ex17-test2.txt for argument use. This script copyies files.
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print("Copying from %s to %s" % (from_file, to_file))

#We could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()
#indata = open(from_file).read()

print("The input file is %d bytes long" % len(indata))

print("Does the output file exist? %r" % exists(to_file))
print("Ready, hit RETURN to continue, CTRL-C to abort."),
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright. All done.")

out_file.close()
in_file.close()
#If you are using one line for lines 9 and 10, you do not
#need line 25, as in_file isn't defined.