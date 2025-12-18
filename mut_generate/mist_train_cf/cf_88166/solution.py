"""
QUESTION:
Create a function named `min_operations` that takes a string as input and returns the minimal number of division/multiplication operations needed to make all characters within the string the same. The string length will be between 1 and 100, and it may contain lowercase and uppercase alphabets, special characters, numbers, and spaces. The function should calculate the minimal number of operations by finding the maximum occurrence of any character in the string and subtracting this value from the total length of the string.
"""

def min_operations(s):
    # Count the occurrences of each character in the string
    char_counts = {}
    for char in s:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    
    # Find the character with the maximum occurrence
    max_occurrence = max(char_counts.values())
    
    # Calculate the minimal number of operations needed
    min_operations = len(s) - max_occurrence
    
    return min_operations