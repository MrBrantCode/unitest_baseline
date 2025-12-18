"""
QUESTION:
Create a function named `compare_strings` that takes two strings as arguments and returns a boolean value indicating whether the two strings contain the same characters, regardless of their order, ignoring case and whitespace characters.
"""

def compare_strings(str1, str2):
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