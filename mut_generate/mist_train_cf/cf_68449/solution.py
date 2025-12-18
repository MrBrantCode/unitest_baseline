"""
QUESTION:
Implement the `is_ecstatic` function, which checks whether a given string `s` meets the ecstatic standard. The string is considered ecstatic if it has a minimum length of 5, all characters in any 5 consecutive positions are unique, each unique character appears at least three times, there are no consecutive repeating letters, and the total count of each unique character is divisible by 3.
"""

def is_ecstatic(s):
    """
    Checks if a given string meets the ecstatic standard.

    A string is considered ecstatic if it has a minimum length of 5, all characters in any 5 consecutive positions are unique, 
    each unique character appears at least three times, there are no consecutive repeating letters, and the total count of each 
    unique character is divisible by 3.

    Args:
        s (str): The input string to be checked.

    Returns:
        bool: True if the string is ecstatic, False otherwise.
    """
    
    from collections import deque

    if len(s) < 5:
        return False

    hash_map = {}
    unique_chars = set(s)
    prev_char = deque(s)
    
    # Ensuring that every unique character appears not less than thrice
    for char in unique_chars:
        if s.count(char) < 3:
            return False
        # Add character occurrences to hashmap
        hash_map[char] = s.count(char)
        
    # Ensure string void of back-to-back repeating letters
    prev_char.popleft()
    prev_char.append(None)
    for a, b in zip(s, prev_char):
        if a == b:
            return False

    # Ensure the cumulative number of occurrences for every unique character is divisible by 3
    for key in hash_map:
        if hash_map[key] % 3 != 0:
            return False

    return True