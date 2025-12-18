"""
QUESTION:
Implement a function `reverse_concatenate(string1, string2)` that takes two input strings `string1` and `string2` and returns their concatenated string in reverse order without using any built-in string concatenation or joining functions. The function should manually implement the concatenation algorithm and store the result in a separate variable.
"""

def reverse_concatenate(string1, string2):
    # Get the lengths of the strings
    len1 = len(string1)
    len2 = len(string2)
    
    # Create an empty list to store the characters of the final string
    final_string = []
    
    # Iterate over string2 and append its characters to the final string list
    for i in range(len2 - 1, -1, -1):
        final_string.append(string2[i])
    
    # Iterate over string1 and append its characters to the final string list
    for i in range(len1 - 1, -1, -1):
        final_string.append(string1[i])
    
    # Convert the final string list into a string
    final_string = ''.join(final_string)
    
    return final_string