"""
QUESTION:
Create a function `dominant_character_robust` that takes a string and an integer `k` as input, where `k` is less than or equal to the length of the string. The function should return the character that appears more than `⌊N/K⌋` times, where `N` is the length of the string. If multiple characters meet this criteria, return the one that appears first in the string. If no such character exists, return "None". The function should operate in O(N) time complexity and O(N) space complexity.
"""

from collections import OrderedDict 

def dominant_character_robust(string: str, k: int) -> str:
    result = "None"
    minimum_count = len(string) // k
    char_count = OrderedDict()
    
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
            
        if result == "None" and char_count[char] > minimum_count:
            result = char

    return result