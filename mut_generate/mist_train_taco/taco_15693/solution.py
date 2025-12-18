"""
QUESTION:
Given a number d, representing the number of digits of a number. Find the total count of positive integers which have at-least one zero in them and consist d or less digits.
Example 1:
Input: d = 2
Output: 9 
Explanation: There are total 9 
positive integers which have 
at-least one zero in them 
and consist 2 or less digits.
Example 2:
Input: d = 3
Output: 180
Explanation: There are total 180
positive integers which have
at-least one zero in them
and consist 3 or less digits.
Your Task:  
You dont need to read input or print anything. Complete the function findCountUpto() which takes d as input parameter and returns the total count of positive integers which have at-least one zero in them and consist d or less digits.
Expected Time Complexity: O(logn)
Expected Auxiliary Space: O(1)
Constraints:
1<= d <=15
"""

def find_count_upto(d: int) -> int:
    return 9 * (10 ** d - 1) // 9 - 9 * (9 ** d - 1) // 8