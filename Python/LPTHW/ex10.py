tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnp\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
# Raw fat cat for example of %r
print "%r" % fat_cat