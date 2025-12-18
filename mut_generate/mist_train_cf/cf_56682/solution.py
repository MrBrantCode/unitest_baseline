"""
QUESTION:
Construct a function `count_letters(s)` that takes a string `s` as input and returns a dictionary where the keys are the distinct alphabets present in the string and the values represent the frequency of each letter. The function should only count alphabetic characters and should be case sensitive, treating 'a' and 'A' as two different characters.
"""

def count_letters(s):
    result = {}
    for letter in s:
        if letter.isalpha():  
            if letter in result:  
                result[letter] += 1
            else:
                result[letter] = 1  
    return result