"""
QUESTION:
Write a function `begin_end_same(input_string, exclude_chars=None)` that takes an input string and an optional list of excluded characters as parameters. The function should return a boolean value indicating whether every word in the string, excluding words containing any character from the exclusion list, begins and ends with the same letter.
"""

def begin_end_same(input_string, exclude_chars=None):
    # If there's no exclusion list provided, make it an empty set for efficiency
    exclude_chars = set(exclude_chars) if exclude_chars else set()
    
    for word in input_string.split():
        # If the word contains any char from the exclusion set, skip it
        if any(ch in exclude_chars for ch in word):
            continue
        
        # Check if the first character is same as the last character
        if word[0] != word[-1]:
            return False
    
    # If none of the words fail the check, return True
    return True