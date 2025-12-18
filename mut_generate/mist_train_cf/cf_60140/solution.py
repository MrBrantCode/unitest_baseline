"""
QUESTION:
Design a function `palindrome_check` that determines whether a given string is a palindrome, ignoring case sensitivity, punctuation, and spaces. The function should return True if the string is a palindrome and False otherwise.
"""

def palindrome_check(word):
    word = ''.join(e for e in word if e.isalnum()).lower()
        
    if len(word) <= 1 :
        return True
    else:
        if word[0] == word[-1]:
            return palindrome_check(word[1:-1])
        else:
            return False