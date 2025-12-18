"""
QUESTION:
Given a number N, find the sum of first and last digit of N. 
 
Example 1:
Input: N = 12345
Output: 6
Explanation: 1st and last digits are 1 and 5.
Example 2:
Input: 98562
Output: 11
Explanation: 1st and last digits are 9 and 2. 
 
Your Task:
You don't need to read or print anything. Your task is to complete the function corner_digitSum() which takes N as input parameter and returns the sum of first and last digit of N.
 
Expect Time Compelxity: O(log_{10}(N))
Expected Space Complexity: O(1)
Constraints:
1 <= N <= 10^{9}
"""

def corner_digitSum(n: int) -> int:
    if n < 10:
        return n
    f = str(n)[0]
    l = str(n)[-1]
    return int(f) + int(l)