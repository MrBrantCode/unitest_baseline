"""
QUESTION:
Write a function named `char_count` that takes a string `s` as input and returns the character counts in descending order. The function should output each character and its corresponding count. The input string may contain any characters, including uppercase and lowercase letters, digits, and special characters.
"""

def char_count(s):
    """
    Returns the character counts in descending order.

    Args:
    s (str): The input string.

    Returns:
    dict: A dictionary with characters as keys and their counts as values.
    """
    char_counts = {}
    
    # Count the occurrences of each character in the string
    for char in s:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    
    # Sort the characters based on their occurrence count in descending order
    sorted_chars = sorted(char_counts, key=char_counts.get, reverse=True)
    
    # Print the character counts in descending order
    char_count_dict = {}
    for char in sorted_chars:
        char_count_dict[char] = char_counts[char]
    return char_count_dict