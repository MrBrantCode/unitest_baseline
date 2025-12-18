"""
QUESTION:
Implement a function named `pattern_counter` to calculate the occurrence of distinct, non-overlapping patterns formed by the string "xyz" in a given string. The function should handle cases where the input string is empty and be case sensitive. It should return the count of "xyz" occurrences in the given text.
"""

def pattern_counter(text):
    # Initialize counter to 0
    count = 0
    
    # Check if the text is empty, if true return 0
    if len(text) == 0:
        return count
    
    # Iterate over the string in steps for three, to handle overlapping strings
    for i in range(0, len(text)-2, 3):
        # Check for the pattern and increment counter if found
        if text[i:i+3] == 'xyz':
            count += 1
    return count