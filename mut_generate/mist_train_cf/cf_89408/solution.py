"""
QUESTION:
Write a function named `count_occurrences` that takes two parameters: `string` and `sequence`. The function must return the number of occurrences of `sequence` in `string` with the following conditions: 
- `sequence` is a two-letter string, 
- the two letters in `sequence` must be in the same order and adjacent to each other in `string`, 
- the function is case-insensitive, and 
- `string` can contain uppercase and lowercase letters, spaces, punctuation marks, and special characters.
"""

def count_occurrences(string, sequence):
    count = 0
    sequence = sequence.lower()  # Convert the sequence to lowercase for case-insensitive matching
    
    for i in range(len(string)-1):
        if string[i:i+2].lower() == sequence:
            count += 1
    
    return count