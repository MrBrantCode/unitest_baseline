"""
QUESTION:
Given a list of numbers, write a function `find_pattern(numbers)` that finds and returns the start of the longest repeating pattern within the list. The function should be able to handle patterns of any length. If no repeating pattern is found, it should return `None`.
"""

def find_pattern(numbers):
    patterns = {}  
    max_pattern_length = 0
    max_pattern = None

    for pattern_length in range(1, len(numbers) // 2 + 1):
        for i in range(len(numbers) - pattern_length):
            pattern = tuple(numbers[i:i+pattern_length])  

            if pattern in patterns:
                if pattern_length > max_pattern_length:
                    max_pattern_length = pattern_length
                    max_pattern = pattern
            else:
                patterns[pattern] = i  

    return list(max_pattern) if max_pattern else None