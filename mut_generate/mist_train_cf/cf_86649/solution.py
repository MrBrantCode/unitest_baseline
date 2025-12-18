"""
QUESTION:
Write a recursive function `reverse_string` that takes a string of uppercase letters as input and prints each letter in reverse order. The function should also count the number of vowels in the string and return this count. The input string will have a length between 3 and 15 characters, inclusive.
"""

def reverse_string(s):
    if len(s) == 1:  
        print(s)
        if s in 'AEIOU':  
            return 1  
        else:
            return 0
    else:
        print(s[-1])  
        if s[-1] in 'AEIOU':  
            return 1 + reverse_string(s[:-1])  
        else:
            return reverse_string(s[:-1])  