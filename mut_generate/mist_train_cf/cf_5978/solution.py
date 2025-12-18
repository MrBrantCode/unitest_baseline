"""
QUESTION:
Write a function `compare_strings(str1, str2)` that takes two strings as arguments and returns `True` if they contain the same characters, regardless of their order, and `False` otherwise. The function should consider uppercase and lowercase characters as the same, ignore any whitespace characters, and handle special characters and symbols. It should also handle strings with multiple occurrences of the same character correctly.
"""

def are_anagrams(str1, str2):
    # Remove whitespace characters and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Create a dictionary to count the occurrences of each character in both strings
    count1 = {}
    count2 = {}
    
    for char in str1:
        count1[char] = count1.get(char, 0) + 1
    
    for char in str2:
        count2[char] = count2.get(char, 0) + 1
    
    # Check if the dictionaries have the same keys and values
    return count1 == count2