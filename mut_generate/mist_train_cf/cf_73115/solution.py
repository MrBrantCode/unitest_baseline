"""
QUESTION:
Write a function `count_palindromes` that calculates the recurrence rate of palindromic sequences found within the input text. The function should take a string `text` as input and return the total count of all palindromic substrings, including both entire words and partial substrings, with a minimum length of 2.
"""

def count_palindromes(text):
    count = 0
    for length in range(2, len(text) + 1):  
        for start in range(len(text) - length + 1):  
            substring = text[start:start+length]
            if substring == substring[::-1]:  
                count += 1
    return count