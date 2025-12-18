"""
QUESTION:
Given a number n. The task is to find the smallest number whose factorial contains at least n trailing zeroes.
Example 1:
Input:
n = 1
Output: 5
Explanation : 5! = 120 which has at
least 1 trailing 0.
Example 2:
Input:
n = 6
Output: 25
Explanation : 25! has at least
6 trailing 0.
User Task:
Complete the function findNum() which takes an integer N as input parameters, and returns the answer.
Expected Time Complexity: O(log_{2} N * log_{5} N).
Expected Auxiliary Space: O(1).
Constraints:
1 <= n <= 10^{4}
"""

def find_smallest_factorial_with_trailing_zeroes(n: int) -> int:
    count = 0
    num = 5
    while True:
        temp = num
        while temp % 5 == 0:
            count += 1
            temp //= 5
        if count >= n:
            return num
        num += 5