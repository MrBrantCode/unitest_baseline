"""
QUESTION:
Create a function called `reverse_string` that takes a string `s` as input and returns its reversed version. The input string will only contain alphabetic characters and will have a maximum length of 100 characters. The function should run in O(n) time complexity, where n is the length of the input string, and may use constant space complexity.
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