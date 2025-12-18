"""
QUESTION:
Write a Python function `is_anagram(string1, string2)` that takes two strings as parameters and returns True if the first string is an anagram of the second string, and False otherwise. The function should have a time complexity of O(n), where n is the length of the strings, and a space complexity of O(1). The strings are assumed to contain only lowercase English letters.
"""

def is_anagram(string1, string2):
    if len(string1) != len(string2):
        return False
    
    char_counts = [0] * 26
    
    for char in string1:
        char_counts[ord(char) - ord('a')] += 1
    
    for char in string2:
        char_counts[ord(char) - ord('a')] -= 1
        
    for count in char_counts:
        if count != 0:
            return False
    
    return True