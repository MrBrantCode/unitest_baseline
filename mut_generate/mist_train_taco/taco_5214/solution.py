"""
QUESTION:
Given a number N,  find if N can be expressed as a + b  such that a and b are prime.
Note: If [a, b] is one solution with a <= b, and [c, d] is another solution with c <= d, and a < c then  [a, b] is considered as our answer.
 
Example 1:
Input:
N = 8
Output:
3 5
Explanation:
3 and 5 are both prime and they
add up to 8.
Example 2:
Input:
N = 3
Output:
-1 -1
Explanation:
There are no solutions to the number 3.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function getPrimes() which takes an integer n as input and returns (a,b) as an array of size 2. 
Note: If no value of (a,b) satisfy the condition return (-1,-1) as an array of size 2.
 
Expected Time Complexity: O(N*loglog(N))
Expected Auxiliary Space: O(N)
 
Constraints:
2 <= N <= 10^{6}
"""

import math

def find_prime_pair(N):
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True
    
    if N < 2:
        return [-1, -1]
    
    if is_prime(N - 2) and N - 2 > 0:
        return [2, N - 2]
    
    for i in range(3, N // 2 + 1, 2):
        if is_prime(i) and is_prime(N - i):
            return [i, N - i]
    
    return [-1, -1]