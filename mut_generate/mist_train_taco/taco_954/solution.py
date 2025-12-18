"""
QUESTION:
Calculate the sum of all the multiples of 3 or 7 below the natural number N.
Example 1:
Input: 10
Output: 25
Explanation:
Numbers that are multiple of 3 or 7
are 3, 6, 7, 9 so sum will be 25.
Example 2:
Input: 25
Output: 84
Explanation: 
Numbers that are multiple of 3 or 7
are 3, 6, 7, 9, 12, 14, 15, 18 so 
sum will be 84.
Your Task:
You don't need to read or print anything. Your task is to complete the function sum() which takes N as input parameter and returns the sum of numbers that are multiple of 3 or 7.
Expected Time Complexity: O(1)
Expected Space Complexity: O(1)
Constraints:
1 <= N <= 1000000
"""

def sum_multiples_of_3_or_7(N: int) -> int:
    total_sum = 0
    for i in range(1, N):
        if i % 3 == 0 or i % 7 == 0:
            total_sum += i
    return total_sum