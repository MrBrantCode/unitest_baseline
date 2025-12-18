"""
QUESTION:
Write a function named `compare_strings` that takes two strings as input and returns the number of differing characters and their positions. The function should consider uppercase and lowercase characters as different. If the strings are of unequal lengths, the extra characters in the longer string are also considered as differing characters.
"""

def compare_strings(string_a, string_b):
    differing_chars = 0
    differing_positions = []
    
    # Make sure both strings have equal length
    length = min(len(string_a), len(string_b))
    
    for i in range(length):
        # Check if the characters are different
        if string_a[i] != string_b[i]:
            differing_chars += 1
            differing_positions.append(i)
    
    # Add any remaining characters from the longer string
    if len(string_a) > length:
        differing_chars += len(string_a) - length
        differing_positions.extend(range(length, len(string_a)))
    elif len(string_b) > length:
        differing_chars += len(string_b) - length
        differing_positions.extend(range(length, len(string_b)))
    
    return differing_chars, differing_positions