"""
QUESTION:
Create a function named `is_anagram` that checks if two input strings are anagrams of each other. The function should handle strings with spaces and special characters, be case-sensitive, and exclude empty strings or strings containing only spaces. Implement the function without using built-in string manipulation functions or libraries.
"""

def is_anagram(str1, str2):
    # Check if either string is empty or contains only spaces
    if str1.strip() == '' or str2.strip() == '':
        return False
    
    # Remove spaces and special characters from both strings
    str1 = ''.join(c for c in str1 if c.isalnum())
    str2 = ''.join(c for c in str2 if c.isalnum())

    # Check if the lengths of the modified strings are equal
    if len(str1) != len(str2):
        return False
    
    # Count the occurrence of each character in both strings
    count = [0] * 128  # Assuming ASCII characters
    
    for i in range(len(str1)):
        count[ord(str1[i])] += 1
        count[ord(str2[i])] -= 1
    
    # Check if the count arrays are equal
    for i in count:
        if i != 0:
            return False
    
    return True