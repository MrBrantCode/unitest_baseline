"""
QUESTION:
Write a function called `is_ecstatic` that takes a string `s` as input. The function should return `true` if the string meets the following conditions, and `false` otherwise:
- The length of the string is at least 5.
- Every unique character in the string appears at least 3 times.
- No character appears consecutively (back-to-back).
- The total number of occurrences of each unique character is divisible by 3.
"""

def is_ecstatic(s):
    """
    Returns True if the string meets the conditions, False otherwise.
    
    Conditions:
    - The length of the string is at least 5.
    - Every unique character in the string appears at least 3 times.
    - No character appears consecutively (back-to-back).
    - The total number of occurrences of each unique character is divisible by 3.
    """
    
    # Check if the length of the string is at least 5
    if len(s) < 5:
        return False
    
    # Create a dictionary to store the count of each unique character
    char_count = {}
    
    # Create a set to store unique characters
    unique_chars = set(s)
    
    # Iterate over each unique character
    for char in unique_chars:
        # Count the occurrences of the character
        count = s.count(char)
        
        # Check if the character appears at least 3 times
        if count < 3:
            return False
        
        # Store the count in the dictionary
        char_count[char] = count
    
    # Check for consecutive characters
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return False
    
    # Check if the total number of occurrences of each unique character is divisible by 3
    for count in char_count.values():
        if count % 3 != 0:
            return False
    
    # If all conditions are met, return True
    return True