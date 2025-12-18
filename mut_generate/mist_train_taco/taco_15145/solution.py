"""
QUESTION:
You are given a number 'n'. Your task is to check whether the power of its largest prime factor is greater than one or not.
Print "YES" if the power is greater than one otherwise print "NO".
Example 1:
Input: n = 36
Output: YES
Explaination: The largest prime which divides 
36 is 3. And it has power = 2 (2*2*3*3)
Example 2:
Input: n = 13
Output: NO
Explaintion: The largest prime which divides 
13 is 13 itself.
Your Task:
You do not need to read input or print anything. Your task is to complete the function largePrime() which takes n as input parameter and returns 1 if the largest prime which divides n has power greater than 1, else, returns 0.
Expected Time Complexity: O(log(n))
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ n ≤ 10^{18}
"""

def is_largest_prime_factor_power_greater_than_one(n: int) -> int:
    i = 2
    prime_factors = {}
    
    # Factorize n
    while i * i <= n:
        while n % i == 0:
            if i in prime_factors:
                prime_factors[i] += 1
            else:
                prime_factors[i] = 1
            n = n // i
        i += 1
    
    # If n is still greater than 1, it is a prime factor
    if n > 1:
        prime_factors[n] = 1
    
    # If no prime factors found, return 0
    if not prime_factors:
        return 0
    
    # Find the largest prime factor and check its power
    largest_prime_factor = max(prime_factors)
    if prime_factors[largest_prime_factor] > 1:
        return 1
    else:
        return 0