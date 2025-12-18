"""
QUESTION:
Given a number n, the task is to check whether it can be expressed as a sum of two or more consecutive numbers or not.
NOTE: Return "1" if number can be expressed as sum of consecutives else "0". (Without the double quotes)
Example 1:
Input: n = 10
Output: 1 
Explanation: It can be expressed as sum of 
two or more consecutive numbers 1+2+3+4.
Example 2:
Input: n = 16
Output: 0
Explanation: It cannot be expressed as 
sum of two or more consecutive numbers.
Your Task:  
You dont need to read input or print anything. Complete the function canBeSumofConsec() which takes n as input parameter and returns  1 if number can be expressed as sum of consecutives else 0.
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
Constraints:
1<= n <=10^{18}
"""

def canBeSumofConsec(n: int) -> int:
    if n & (n - 1):
        return 1
    return 0