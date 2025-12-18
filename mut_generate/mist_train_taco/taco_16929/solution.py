"""
QUESTION:
Given a number n, the task is to calculate its primorial. Primorial of a number is similar to factorial of a number. In primorial, not all the natural numbers get multiplied; only prime numbers are multiplied to calculate the primorial of a number. It is denoted with P#.
 
Example 1:
Input:
N = 5
Output: 30
Explanation:
Priomorial = 2 * 3 * 5 = 30
As a side note, factorial is 2 * 3 * 4 * 5
 
Example 2:
Input:
N = 12
Output: 2310
Your Task:  
You don't need to read input or print anything. Your task is to complete the function primorial() which takes the integer N as input parameters and returns the primorial of number n. Since the answer can be quite large print it modulo 10^{9}+7.
Expected Time Complexity: O(N*sqrt(N))
Expected Auxiliary Space: O(1)
 
Constraints:
1 ≤ N ≤ 10^{5}
"""

def calculate_primorial(N: int) -> int:
    MOD = 1000000007
    
    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    primorial_value = 1
    for i in range(2, N + 1):
        if is_prime(i):
            primorial_value = (primorial_value * i) % MOD
    
    return primorial_value