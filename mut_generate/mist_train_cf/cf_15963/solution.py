"""
QUESTION:
Write a function `reverse_string` that takes a string `s` as input, where `s` contains only alphabetic characters and has a maximum length of 100 characters. The function should return a reversed version of `s` without using any built-in string reversal functions or methods, and should achieve this in O(n) time complexity, where n is the length of `s`, using constant space complexity.
"""

def reverse_string(s):
    # Convert the string into a list of characters
    chars = list(s)
    
    # Initialize two pointers, one at the beginning and one at the end of the list
    start = 0
    end = len(chars) - 1
    
    # Swap characters from start to end until the two pointers meet in the middle
    while start < end:
        chars[start], chars[end] = chars[end], chars[start]
        start += 1
        end -= 1
    
    # Convert the list back into a string
    reversed_string = ''.join(chars)
    
    return reversed_string