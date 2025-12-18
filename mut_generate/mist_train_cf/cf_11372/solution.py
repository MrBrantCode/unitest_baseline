"""
QUESTION:
Write a function named `isUniqueString` that takes a string as input and returns a boolean indicating whether the string contains all unique characters, without using any additional data structures. The function should not assume any specific character set or case sensitivity. The input string can be empty.
"""

def isUniqueString(s):
    """
    Checks if a given string contains all unique characters without using any additional data structures.

    Args:
        s (str): The input string.

    Returns:
        bool: True if the string contains all unique characters, False otherwise.
    """
    
    # Initialize a boolean variable isUnique to True
    isUnique = True
    
    # Iterate through each character in the string
    for i in range(len(s)):
        # Iterate through the rest of the characters in the string
        for j in range(i + 1, len(s)):
            # If a match is found, set isUnique to False and break out of both loops
            if s[i] == s[j]:
                isUnique = False
                break
        
        # If isUnique is False, break out of the outer loop
        if not isUnique:
            break
    
    # Return the result
    return isUnique