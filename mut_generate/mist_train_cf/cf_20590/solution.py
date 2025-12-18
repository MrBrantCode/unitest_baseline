"""
QUESTION:
Write a function `compare_strings(str1, str2)` that takes two strings as input and returns `True` if the strings contain the same characters, regardless of their order, and `False` otherwise. The function should consider uppercase and lowercase characters as the same, ignore any whitespace characters, and handle special characters and symbols. The function should also handle strings with multiple occurrences of the same character correctly.
"""

def compare_strings(str1, str2):
    # Remove whitespace characters from the strings
    str1 = str1.replace(" ", "")
    str2 = str2.replace(" ", "")
    
    # Convert the strings to lowercase
    str1 = str1.lower()
    str2 = str2.lower()
    
    # Create dictionaries to count the occurrences of each character in the strings
    count1 = {}
    count2 = {}
    
    # Count the occurrences of each character in string 1
    for char in str1:
        if char in count1:
            count1[char] += 1
        else:
            count1[char] = 1
    
    # Count the occurrences of each character in string 2
    for char in str2:
        if char in count2:
            count2[char] += 1
        else:
            count2[char] = 1
    
    # Compare the dictionaries
    return count1 == count2