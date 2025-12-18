"""
QUESTION:
Create a function `check_anagram(str1, str2)` that determines whether two given strings are anagrams of each other. The function should consider case-sensitivity, special characters, and numbers in its validation. The strings may contain special characters and numbers. The function should return True if the strings are anagrams, and False otherwise.
"""

def check_anagram(str1, str2):
    """
    Determine whether two given strings are anagrams of each other.
    
    Args:
        str1 (str): The first string.
        str2 (str): The second string.
    
    Returns:
        bool: True if the strings are anagrams, False otherwise.
    """
    # Create hash map
    map = {}
    
    # Count frequency of each character in first string
    for char in str1:
        if char in map:
            map[char] += 1
        else:
            map[char] = 1
    
    # Decrease frequency of each character in second string
    for char in str2:
        if char in map:
            map[char] -= 1
        else:
            return False
    
    # Check if all frequencies are zero
    for key in map:
        if map[key] != 0:
            return False

    return True