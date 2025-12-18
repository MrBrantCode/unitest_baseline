"""
QUESTION:
Create a function named `generate_output_string` that takes two input strings `str1` and `str2` of equal length. The function should return a string containing alternate characters from `str1` and `str2`, without any repeated characters, and sorted in ascending order.
"""

def generate_output_string(str1, str2):
    output = ''
    i = 0
    j = 0
    
    while i < len(str1) and j < len(str2):
        if str1[i] not in output:
            output += str1[i]
        if str2[j] not in output:
            output += str2[j]
        
        i += 1
        j += 1
    
    # Add remaining characters from str1, if any
    while i < len(str1):
        if str1[i] not in output:
            output += str1[i]
        i += 1
    
    # Add remaining characters from str2, if any
    while j < len(str2):
        if str2[j] not in output:
            output += str2[j]
        j += 1
    
    # Sort the output string in ascending order
    output = ''.join(sorted(output))
    
    return output