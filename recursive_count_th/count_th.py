'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    occurences = 0

    #If the word is one character, it can't contain any th's, return false
    if len(word) < 2:
        return 0
    #if the words first two characters are th return true
    if word[0:2] == "th":
        occurences += 1
    #Recurse down the length of the word to discover all present th's
    return occurences + count_th(word[1:])
   
