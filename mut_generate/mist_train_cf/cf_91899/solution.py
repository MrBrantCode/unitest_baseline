"""
QUESTION:
Create a function called `min_operations` that takes a string of lowercase alphabets as input and returns the minimum number of division/multiplication operations needed to make all characters within the string the same. The input string length will be between 1 and 100.
"""

def min_operations(s):
    operations = 0
    
    # Count the frequency of each character
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    
    # Find the character with the maximum frequency
    max_freq = max(freq.values())
    
    # Calculate the minimum number of operations
    for char in freq:
        operations += abs(freq[char] - max_freq)
    
    return operations