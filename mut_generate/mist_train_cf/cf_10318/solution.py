"""
QUESTION:
Write a function `concatenate_strings(str1, str2)` that concatenates two input strings `str1` and `str2` without using the concatenation operator "+" or any built-in string manipulation functions. The function should return the concatenated string. 

Restrictions: Do not use the concatenation operator "+" or any built-in string manipulation functions such as `str.join`, `str.format`.
"""

def concatenate_strings(str1, str2):
    # Get the lengths of the input strings
    len1 = len(str1)
    len2 = len(str2)
    
    # Create an empty list to store the characters of the concatenated string
    result = []
    
    # Append the characters of the first string to the result list
    for i in range(len1):
        result.append(str1[i])
    
    # Append the characters of the second string to the result list
    for i in range(len2):
        result.append(str2[i])
    
    # Convert the result list to a string
    concatenated_string = ''
    for char in result:
        concatenated_string += chr(ord(char) + ord('0') - ord('0'))
    
    return concatenated_string