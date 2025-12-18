"""
QUESTION:
Given a number N, find the even factor sum of the number N.
 
Example 1:
Input: 
N = 30 
Output: 
48 
Explanation:
Even dividers sum 2 + 6 + 10 + 30 = 48
Example 2:
Input: 
N = 18 
Output: 
26 
Explanation:
Even dividers sum 2 + 6 + 18 = 26
Your Task:
You don't need to read input or print anything. Your task is to complete the function evenFactors() which takes an integer N as input parameters and returns an integer, number of even factors of N.
 
Expected Time Complexity: O(sqrt(N))
Expected Space Complexity: O(1)
 
Constraints:
1 <= N <= 10^{9}
"""

def sum_of_even_factors(N: int) -> int:
    sum_even_factors = 0
    for i in range(2, N + 1, 2):  # Start from 2 and increment by 2 to ensure i is even
        if N % i == 0:
            sum_even_factors += i
    return sum_even_factors