"""
QUESTION:
Given a number N find how many integers from 1 to N contains 0's as a digit. 
 
Example 1:
Input: N = 20
Output: 2
Explanation: 10 and 20 has '0' as a digit.
Example 2:
Input: N = 100
Output: 10
Explanation: 10, 20, 30, 40, 50, 60, 70,
80, 90, 100 has '0' as a digit.
 
Your Task:
You don't need to read or print anything. Your task is to complete the function CountNo() which takes N as input parameter and returns the count of numbers which contains '0' as a digit.
 
Expected Time Complexity: O(N * log_{10}(N))
Expected Space Complexity: O(1)
 
Constraints:
1 <= N <= 10000
"""

def count_numbers_with_zero(N: int) -> int:
    count = 0
    for x in range(1, N + 1):
        while x > 0:
            if x % 10 == 0:
                count += 1
                break
            x = x // 10
    return count