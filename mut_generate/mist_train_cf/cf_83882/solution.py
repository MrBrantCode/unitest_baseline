"""
QUESTION:
Write a function `count_pattern` that takes two parameters, a string and a pattern, and returns the number of non-overlapping occurrences of the pattern in the string, considering case sensitivity.
"""

def count_pattern(string, pattern):
    
    # Convert the string and pattern to lowercase to ensure case sensitivity
    string_lower = string.lower()
    pattern_lower = pattern.lower()

    # Initialize count to 0
    count = 0

    # Search for pattern from start to end in the string
    start = 0
    while start < len(string):
        pos = string_lower.find(pattern_lower, start)

        # If pattern found, increment count and update start position for next search
        if pos != -1:
            start = pos + 1
            count += 1
        else:
            break

    # Return the count
    return count