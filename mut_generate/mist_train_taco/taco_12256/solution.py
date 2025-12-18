"""
QUESTION:
Given a number, N. Find the sum of all the digits of N
 
Example 1:
Input:
N = 12
Output:
3
Explanation:
Sum of 12's digits:
1 + 2 = 3
Example 2:
Input:
N = 23
Output
5
Explanation:
Sum of 23's digits:
2 + 3 = 5
Your Task:
You don't need to read input or print anything. Your task is to complete the function sumOfDigits() which takes an integer N as input parameters and returns an integer, total sum of digits of N.
Expected Time Complexity: O(log_{10}N)
Expected Space Complexity: O(1)
 
Constraints:
1<=N<=10^{5}
"""

def sum_of_digits(N: int) -> int:
    sd = 0
    num = N
    while num > 0:
        ld = num % 10
        sd += ld
        num = num // 10
    return sd