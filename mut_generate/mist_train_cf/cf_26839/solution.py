"""
QUESTION:
Write a function `calculate_frequency(S1: str, S2: str) -> int` that calculates the sum of the frequencies of characters in string S2, where the frequency of each character is determined by its occurrence in string S1. The function should be case-sensitive and only consider characters present in S1. The length of both strings should be between 1 and 10^5.
"""

def calculate_frequency(S1: str, S2: str) -> int:
    char_frequency = {}
    for char in S1:
        char_frequency[char] = char_frequency.get(char, 0) + 1
    
    return sum(char_frequency[char] for char in S2 if char in char_frequency)