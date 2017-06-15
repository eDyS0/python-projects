"""
Checks if the string entered by the user is a palindrome. That is that it reads the same forwards as backwards like “racecar”
"""
def palindrome(string):
    string = string.lower()
    l = len(string) // 2
    if len(string) % 2 == 0:
        return (string[:l] == string[l:][::-1])
    return (string[:l] == string[l+1:][::-1])
