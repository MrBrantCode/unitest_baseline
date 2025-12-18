"""
QUESTION:
A palindromic prime (sometimes called a palprime) is a prime number that is also a palindromic number.Given a number n, output the count of numbers less than or equal to n which are palindromic prime.
 
Example 1:
Input:
n = 3
Output:
2
Explanation:
There are 2 palprimes less than or
equal to 3. They are 2, and 3.
Example 2:
Input:
n = 12
Output:
5
Explanation:
There are 5 palprimes less than or
equal to 12. They are 2, 3, 5, 7, and 11.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function palPrimes() which takes an Integer n as input and returns the number of palprimes less than or equal to n.
 
Expected Time Complexity: O(n*(log(log(n))))
Expected Auxiliary Space: O(n)
 
Constraints:
1 <= n <= 10^{6}
"""

import math

def is_prime(n):
    if n <= 1:
        return False
    max_div = math.floor(math.sqrt(n))
    for i in range(2, max_div + 1):
        if n % i == 0:
            return False
    return True

def count_palindromic_primes(n):
    count = 0
    for i in range(n + 1):
        x = str(i)
        if x == x[::-1]:
            if is_prime(i):
                count += 1
    return count