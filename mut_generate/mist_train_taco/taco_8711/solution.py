"""
QUESTION:
Given a date, the task is to check if it is valid or not. It may be assumed that the given date is in range from 01/01/1800 to 31/12/9999 and any date not within this range will also be considered invalid.
 
Example 1:
Input:
d = 10, m = 12, y = 2000
Output:
1
Explanation:
The given date 10/12/2000 is valid.
Example 2:
Input:
d = 30, m = 2, y = 1700
Output:
0
Explanation:
The given date 30/2/1700 is invalid.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function isValidDate() which takes 3 Integers d,m and y as input and returns the answer.
 
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= d, m, y <= 10000
"""

def is_valid_date(d: int, m: int, y: int) -> int:
    # List of months with 31 days
    mon_31 = [1, 3, 5, 7, 8, 10, 12]
    
    # Check if the year is within the valid range
    if y < 1800 or y > 9999:
        return 0
    
    # Check for months with 31 days
    if m in mon_31:
        if d < 1 or d > 31:
            return 0
    # Check for months with 30 days
    elif m in [4, 6, 9, 11]:
        if d < 1 or d > 30:
            return 0
    # Check for February
    elif m == 2:
        # Check for leap year
        if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
            if d < 1 or d > 29:
                return 0
        else:
            if d < 1 or d > 28:
                return 0
    else:
        return 0
    
    return 1