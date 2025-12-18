"""
QUESTION:
Write a function named `count_a` that takes a string as input and returns the number of times the letter 'a' appears in the string, excluding any occurrences of 'a' that are immediately followed by 'b'.
"""

def count_a(input_string):
    count = 0
    i = 0
    while i < len(input_string):
        if input_string[i] == 'a':
            if i + 1 < len(input_string) and input_string[i+1] == 'b':
                i += 1  # Skip 'b' after 'a'
            else:
                count += 1  # Increment count for 'a'
        i += 1
    return count