"""
QUESTION:
As we know that every number >=2 can be represented as natural powers of primes(prime factorization). Also prime factorization is unique for a number. 
Eg. 360 = 2^{3}3^{2}5^{1}
Today we are interested in geek numbers. A geek number is a number whose prime factorization only contains powers of unity.Below are some geek numbers.
Eg. 2 = 2^{1}
    22 = 2^{1}11^{1}
Example 1:
Input: N = 22
Output: Yes
Explaination: 22 = 2^{1}11^{1}. Where all the 
powers of prime numbers are one.
Example 2:
Input: N = 4
Output: No
Explaination: 4 = 2^{2}. Where all the 
powers of all the prime are not one.
Your Task:
You do not need to read input or print anything. Your task is to complete the function geekNumber() which takes N as input parameter and returns 1 if it a geek number. Otherwise, returns 0.
Expected Time Complexity: O(sqrt(N))
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ N ≤ 10^{6}
"""

def is_geek_number(n: int) -> int:
    if n in [1, 2, 3]:
        return 1
    
    k = int(n ** 0.5 + 0.5)
    for i in range(2, k + 1):
        if n % i == 0:
            if n % (i ** 2) == 0:
                return 0
    
    return 1