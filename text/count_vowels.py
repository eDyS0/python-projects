"""
Enter a string and the program counts the number of vowels in the text. For added complexity have it report a sum of each vowel found.
"""

def count_vowels(string):
    d = {'a':0,'e':0,'i':0,'o':0,'u':0,'y':0}
    for c in string.lower():
        if c in d:
            d[c] += 1
    return(d)
