"""
QUESTION:
Create a recursive function called `is_reverse_anagram` that takes a single string input, including symbols and numbers. The function should return True if the input string is an anagram of its reverse, and False otherwise, without using built-in reverse or sort functions.
"""

def is_reverse_anagram(word):
    # base case: if the length of the word is 1 or 0
    if len(word) <= 1:
        return True
    
    # case: if the first letter is the same as the last letter
    elif word[0] == word[-1]:
        return is_reverse_anagram(word[1:-1])
        
    # case: if the first letter is not the same as the last letter
    else:
        return False