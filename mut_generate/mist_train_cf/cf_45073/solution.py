"""
QUESTION:
Design a function `float_common` that takes a set of unique float strings as input and returns the digit that appears most frequently across all floats. If multiple digits appear with the same maximum frequency, return the smallest digit. The function should have a low time complexity and assume standard decimal system representation (0-9).
"""

from collections import Counter

def float_common(floats):
    counters = Counter(char for float_str in floats for char in float_str if char != '.')
    max_frequency = max(counters.values())
    most_common_chars = sorted(key for key, value in counters.items() if value == max_frequency)
    
    return int(most_common_chars[0])