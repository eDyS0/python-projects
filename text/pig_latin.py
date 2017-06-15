"""
Pig Latin – Pig Latin is a game of alterations played on the English language game. 
To create the Pig Latin form of an English word the initial consonant sound is transposed to the end of the word and an ay is affixed 
"""
def pig_latin(string):
    v = 'aeiouAEIOU' #list of vowels
    if string[0] in v:
        return (string+"-way")
    else:
        for n, c in enumerate(string):
            if c in v:
                return (string[n:].title()+'-'+string[:n].lower()+'ay')
