"""
QUESTION:
Given a positive integer N. The task is to check whether a number has exactly three distinct factors or not. 
 
Example 1:
Input:
N = 10
Output:
0
Explanation:
10 has 4 factors- 1,2,5 and 10.
So, the Ouput is 0.
Example 2:
Input:
N = 9
Output:
1
Explanation:
9 has 3 factors- 1,3 and 9.
So, the Ouput is 1.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function hasThreePrimeFac() which takes an Integer N as input and returns 1 if it has exactly 3 factors else returns 0.
 
Expected Time Complexity: O(sqrt(N))
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= N <= 10^{12}
"""

def has_exactly_three_factors(N: int) -> int:
    def is_prime(n: int) -> bool:
        if n <= 1:
            return False
        k = int(n ** 0.5)
        for i in range(2, k + 1):
            if n % i == 0:
                return False
        return True
    
    sqrt_N = int(N ** 0.5)
    if sqrt_N * sqrt_N == N:
        if is_prime(sqrt_N):
            return 1
    return 0