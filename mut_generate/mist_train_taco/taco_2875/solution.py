"""
QUESTION:
Given a natural number N, the task is to find the sum of the divisors of all the divisors of N.
Example 1:
Input:
N = 54
Output:
232
Explanation:
Divisors of 54 = 1, 2, 3, 6, 9, 18, 27, 54.
Sum of divisors of 1, 2, 3, 6, 9, 18, 27, 54 
are 1, 3, 4, 12, 13, 39, 40, 120 respectively.
Sum of divisors of all the divisors of 54
 = 1 + 3 + 4 + 12 + 13 + 39 + 40 + 120 = 232.
Example 2:
Input:
N = 10
Output:
28
Explanation:
Divisors of 10 are 1, 2, 5, 10
Sums of divisors of all the divisors are 
1, 3, 6, 18.
Overall sum = 1 + 3 + 6 + 18 = 28
Your Task:  
You don't need to read input or print anything. Your task is to complete the function sumOfDivisors() which takes an integer N as an input parameter and return the sum of the divisors of all the divisors of N.
Expected Time Complexity: O(NloglogN)
Expected Auxiliary Space: O(N)
Constraints:
1 <= N <= 10^{4}
"""

def sum_of_divisors_of_divisors(N: int) -> int:
    total_sum = 0
    for i in range(1, N + 1):
        if N % i == 0:
            for j in range(1, i + 1):
                if i % j == 0:
                    total_sum += j
    return total_sum