"""
QUESTION:
Balance strings, by definition, are the strings that contain all the characters of the alphabet, from a to z, equal no of times.
eg- abcdefghijklmnopqrstuvwxyz is a balanced string, aabb is not.

Input:
First line contains number of test cases T. Each test case contains a string S which made up of only lowercase characters.  

Output:
For each test case print Yes if the string is balanced string else print No.  

Constraints: 
1 ≤ T ≤ 10
1 ≤ |S| ≤ 1000   

SAMPLE INPUT
2
codemyca
abcdefghijklmnopqrstuvwxyz

SAMPLE OUTPUT
No
Yes
"""

import string

def is_balanced_string(s: str) -> bool:
    """
    Check if the given string is a balanced string.

    A balanced string is defined as a string that contains all characters from 'a' to 'z' 
    exactly the same number of times.

    Parameters:
    s (str): The string to be checked.

    Returns:
    bool: True if the string is balanced, False otherwise.
    """
    # Count the frequency of 'a'
    k = s.count('a')
    
    # If 'a' is not present, the string cannot be balanced
    if k == 0:
        return False
    
    # Check the frequency of all characters from 'a' to 'z'
    for ch in string.ascii_lowercase:
        if s.count(ch) != k:
            return False
    
    return True