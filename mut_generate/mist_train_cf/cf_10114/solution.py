"""
QUESTION:
Create a function called `find_uncommon_chars` that takes two strings `str1` and `str2` as input and returns a list of uncommon characters between them. The function should be able to handle strings of up to 1000 characters in length and should have a time complexity of O(n), where n is the length of the longer string.
"""

from collections import defaultdict

def find_uncommon_chars(str1, str2):
    count = defaultdict(int)
    
    # Increment count for each character in str1
    for char in str1:
        count[char] += 1
    
    # Decrement count for each character in str2
    for char in str2:
        count[char] -= 1
    
    # Find uncommon characters
    uncommon_chars = []
    for char, freq in count.items():
        if freq != 0:
            uncommon_chars.append(char)
    
    return uncommon_chars