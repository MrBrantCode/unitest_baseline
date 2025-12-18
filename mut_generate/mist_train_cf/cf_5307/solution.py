"""
QUESTION:
Create a function called `reverse_and_join_strings` that takes two strings as input and returns a single string that is the concatenation of the two input strings in reverse order. The function must check that the length of each input string does not exceed 100 characters and must reverse each string using a single loop.
"""

def reverse_and_join_strings(str1, str2):
    if len(str1) > 100 or len(str2) > 100:
        return "Error: String length exceeds 100 characters."
    
    reversed_str1 = ""
    reversed_str2 = ""
    
    for i in range(len(str1)-1, -1, -1):
        reversed_str1 += str1[i]
    
    for i in range(len(str2)-1, -1, -1):
        reversed_str2 += str2[i]
    
    return reversed_str1 + reversed_str2