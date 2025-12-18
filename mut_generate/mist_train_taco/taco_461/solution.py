"""
QUESTION:
In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", a move consists of either replacing one occurrence of "XL" with "LX", or replacing one occurrence of "RX" with "XR". Given the starting string start and the ending string end, return True if and only if there exists a sequence of moves to transform one string to the other.

Example:


Input: start = "RXXLRXRXL", end = "XRLXXRRLX"
Output: True
Explanation:
We can transform start to end following these steps:
RXXLRXRXL ->
XRXLRXRXL ->
XRLXRXRXL ->
XRLXXRRXL ->
XRLXXRRLX


Note:


       1 <= len(start) = len(end) <= 10000.
       Both start and end will only consist of characters in {'L', 'R', 'X'}.
"""

def can_transform(start: str, end: str) -> bool:
    # Check if the lengths of start and end are the same
    if len(start) != len(end):
        return False
    
    # Initialize pointers for start and end
    i, j = 0, 0
    
    # Iterate through the strings
    while i < len(start) and j < len(end):
        # Skip 'X' characters
        while i < len(start) and start[i] == 'X':
            i += 1
        while j < len(end) and end[j] == 'X':
            j += 1
        
        # If one of the pointers has reached the end, check if both have
        if i == len(start) or j == len(end):
            return i == len(start) and j == len(end)
        
        # If the characters at the current positions are different, return False
        if start[i] != end[j]:
            return False
        
        # If both characters are 'L', 'L' in start should be to the left of 'L' in end
        if start[i] == 'L' and i < j:
            return False
        
        # If both characters are 'R', 'R' in start should be to the right of 'R' in end
        if start[i] == 'R' and i > j:
            return False
        
        # Move to the next characters
        i += 1
        j += 1
    
    # If both pointers have reached the end, return True
    return i == len(start) and j == len(end)