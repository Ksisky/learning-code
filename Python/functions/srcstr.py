#A little function I found off of StackExchange.
#Returns true or false depending whether word is in string.
#Credit:AMACB
def wordsearch(word, string):
    return not(string.find(word) == -1)
