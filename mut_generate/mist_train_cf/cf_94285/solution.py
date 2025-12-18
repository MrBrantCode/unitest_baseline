"""
QUESTION:
Create a function `longest_string` that takes two strings `str1` and `str2` as arguments. The function should return the longest string after removing any duplicate characters. Do not use built-in functions or libraries for removing duplicates; implement this logic manually.
"""

def longest_string(str1, str2):
    def remove_duplicates(str):
        result = ""
        for char in str:
            if char not in result:
                result += char
        return result
    
    if len(str1) > len(str2):
        longest = str1
    else:
        longest = str2
    
    return remove_duplicates(longest)