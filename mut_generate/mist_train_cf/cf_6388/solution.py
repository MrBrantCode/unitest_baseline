"""
QUESTION:
Write a function named `count_occurrences` that takes two parameters, `string` and `sequence`, where `string` is the input string to search in and `sequence` is the specific two-letter sequence to search for. The function should count the number of occurrences of the `sequence` in the `string`, considering the two letters as a single unit and in the same order. The search should be case-insensitive and the function should return the total count of occurrences.
"""

def count_occurrences(string, sequence):
    count = 0
    sequence = sequence.lower()  # Convert the sequence to lowercase for case-insensitive matching
    
    for i in range(len(string)-1):
        if string[i:i+2].lower() == sequence:
            count += 1
    
    return count