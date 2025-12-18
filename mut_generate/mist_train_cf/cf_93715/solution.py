"""
QUESTION:
Create a function called `reverse_concatenate` that takes two strings as input. The function must perform the following operations: 
1. Concatenate the two input strings with a space in between.
2. Reverse the order of the characters in the concatenated string.
3. Remove any duplicate characters from the reversed string. 
Note that the output string may not maintain the original order of characters due to the set operation.
"""

def reverse_concatenate(string1, string2):
    concatenated = string1 + ' ' + string2
    reversed_string = concatenated[::-1]
    unique_string = ''.join(set(reversed_string))
    return unique_string