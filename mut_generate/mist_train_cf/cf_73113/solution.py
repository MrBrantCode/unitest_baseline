"""
QUESTION:
Create a function `find_least_frequent(input_string)` that takes a string of characters (both numeric and alphabetic) as input and prints the character with the lowest frequency in the string. If there are multiple characters with the same least frequency, the function should print one of them.
"""

from collections import Counter

def find_least_frequent(input_string):
    frequency = Counter(input_string)
    min_freq = float('inf')
    least_char = ''
    
    for char, freq in frequency.items():
        if freq < min_freq:
            min_freq = freq
            least_char = char
            
    return least_char