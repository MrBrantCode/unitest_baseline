"""
QUESTION:
Write a function named `reverse_string` that takes a string `s` as input and returns the reversed string. Implement the reverse operation manually without using any built-in functions or methods that directly reverse the string. The solution should have a time complexity of O(n), where n is the length of the input string, and should reverse the string in-place using only a constant amount of extra space. The solution should correctly handle Unicode characters and be able to handle very long strings efficiently.
"""

def reverse_string(s):
    # Convert the string to a list of characters
    chars = list(s)
    
    # Get the length of the string
    length = len(s)
    
    # Iterate through half of the string length
    for i in range(length // 2):
        # Swap the characters at indices i and length - i - 1
        chars[i], chars[length - i - 1] = chars[length - i - 1], chars[i]
    
    # Convert the list back to a string
    reversed_string = ''.join(chars)
    
    return reversed_string