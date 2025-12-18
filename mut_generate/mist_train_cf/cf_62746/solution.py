"""
QUESTION:
Write a function `firstUniqCharacter(s)` that identifies the first unique character in a given string `s` and returns its index. If the string contains only repetitive characters or is empty, the function should return -1. The function should accommodate unusual ASCII symbols and have a time complexity of O(N), where N is the length of the string.
"""

from typing import Optional

def firstUniqChar(s: str) -> int:
    frequency = [0] * 256
    position = [-1] * 256
    for i, char in enumerate(s):
        ascii_val = ord(char)
        if frequency[ascii_val] == 0:
            position[ascii_val] = i
        frequency[ascii_val] += 1   

    min_pos = float('inf')
    for i in range(256):
        if frequency[i] == 1:
            min_pos = min(min_pos, position[i])
    
    return min_pos if min_pos != float('inf') else -1