"""
QUESTION:
Count the occurrences of "co" followed by any character and then "e" in a string.

Create a function called `countCode` that takes a string as input and returns the number of times the pattern "co" followed by any character and then "e" appears in the string. The function should only consider sequences of exactly four characters that match this pattern.
"""

def countCode(str):
    """
    Counts the occurrences of "co" followed by any character and then "e" in a string.
    
    Args:
    str (str): The input string.
    
    Returns:
    int: The number of times the pattern "co" followed by any character and then "e" appears in the string.
    """
    count = 0
    for i in range(len(str) - 3):
        # Check if the current index and the next one make "co" and the character 3 positions later is "e"
        if str[i:i+2] == "co" and str[i+3] == 'e':
            count += 1
    return count