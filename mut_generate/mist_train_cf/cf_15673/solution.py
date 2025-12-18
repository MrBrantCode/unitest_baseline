"""
QUESTION:
Write a function called `reverse_string` that takes a string as input and returns the reversed string without using the `reverse()` function or any built-in string manipulation functions. The function should have a time complexity of O(n) and constant space complexity, where n is the length of the input string. The function should be able to handle strings containing uppercase and lowercase letters, as well as special characters.
"""

def reverse_string(string):
    # Convert the string to a list of characters
    chars = list(string)
    
    # Get the length of the string
    length = len(chars)
    
    # Iterate over the first half of the string
    for i in range(length // 2):
        # Swap the characters at symmetric positions
        chars[i], chars[length - i - 1] = chars[length - i - 1], chars[i]
    
    # Convert the list of characters back to a string
    reversed_string = "".join(chars)
    
    return reversed_string