"""
QUESTION:
Create a function `check_order_with_spaces` that receives two strings `string1` and `string2` as input. The function should check if the characters in `string1` appear in the same order as in `string2`, where each character in `string2` is followed by at least two space characters before the next character. The function should have a time complexity of O(n+m), where n and m are the lengths of `string1` and `string2` respectively.
"""

def check_order_with_spaces(string1, string2):
    # Remove all spaces from string2
    string2 = string2.replace(" ", "")
    
    # Initialize pointers for both strings
    i = 0
    j = 0
    
    # Loop until we reach the end of both strings
    while i < len(string1) and j < len(string2):
        # Check if the characters at the current positions match
        if string1[i] == string2[j]:
            # Move the pointer in string1
            i += 1
        # Move the pointer in string2
        j += 1
    
    # Check if we reached the end of string1
    return i == len(string1)