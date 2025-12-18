"""
QUESTION:
Write a function `reverse_words` that takes a string as input and returns the string with the order of words reversed, without using any built-in string manipulation functions and maintaining constant space complexity (O(1)).
"""

def reverse_words(string):
    # Convert the string into a list of characters
    chars = list(string)
    
    # Reverse the entire string
    reverse_string(chars, 0, len(chars) - 1)
    
    # Reverse each individual word in the string
    start = 0
    end = 0
    while end < len(chars):
        if chars[end] == ' ':
            reverse_string(chars, start, end - 1)
            start = end + 1
        end += 1
    
    # Reverse the last word in the string (if any)
    reverse_string(chars, start, end - 1)
    
    # Convert the list of characters back into a string
    return ''.join(chars)

def reverse_string(chars, start, end):
    while start < end:
        chars[start], chars[end] = chars[end], chars[start]
        start += 1
        end -= 1