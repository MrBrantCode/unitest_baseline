"""
QUESTION:
Write a function named `maxFrequencyChar` that takes a string `str` as input and returns the character that appears most frequently in the string. If multiple characters have the same highest frequency, any one of them can be returned. The function should only consider the characters in the input string, without any additional information or constraints.
"""

def maxFrequencyChar(s):
    max_char = ''
    max_frequency = 0
    hash_table = {}
    
    for char in s:
        if char in hash_table:
            hash_table[char] += 1
        else:
            hash_table[char] = 1
    
    for char in hash_table:
        if hash_table[char] > max_frequency:
            max_frequency = hash_table[char]
            max_char = char
    
    return max_char