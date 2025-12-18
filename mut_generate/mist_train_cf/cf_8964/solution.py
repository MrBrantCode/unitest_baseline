"""
QUESTION:
Write a function `are_anagrams` that compares two input strings and returns `True` if they are anagrams, ignoring any spaces and capitalization. The function should have a time complexity of O(n log n), where n is the length of the input strings, and must not use built-in functions or libraries that directly solve the anagram problem. The function should also handle Unicode characters and special characters properly.
"""

def are_anagrams(str1, str2):
    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Sort the strings
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)
    
    # Compare the sorted strings
    return sorted_str1 == sorted_str2