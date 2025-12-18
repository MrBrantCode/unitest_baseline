"""
QUESTION:
Given are positive integers A and B.
Let us choose some number of positive common divisors of A and B.
Here, any two of the chosen divisors must be coprime.
At most, how many divisors can we choose?Definition of common divisor
An integer d is said to be a common divisor of integers x and y when d divides both x and y.Definition of being coprime
Integers x and y are said to be coprime when x and y have no positive common divisors other than 1.Definition of dividing
An integer x is said to divide another integer y when there exists an integer \alpha such that y = \alpha x.

-----Constraints-----
 - All values in input are integers.
 - 1 \leq A, B \leq 10^{12}

-----Input-----
Input is given from Standard Input in the following format:
A B

-----Output-----
Print the maximum number of divisors that can be chosen to satisfy the condition.

-----Sample Input-----
12 18

-----Sample Output-----
3

12 and 18 have the following positive common divisors: 1, 2, 3, and 6.
1 and 2 are coprime, 2 and 3 are coprime, and 3 and 1 are coprime, so we can choose 1, 2, and 3, which achieve the maximum result.
"""

from math import gcd

def max_coprime_divisors(A, B):
    # Calculate the greatest common divisor (GCD) of A and B
    n = gcd(A, B)
    
    # Initialize the answer to 1 (since 1 is always a common divisor)
    ans = 1
    
    # Initialize the divisor to start checking from 1
    i = 1
    
    # Loop to find all divisors of the GCD
    while i * i < n:
        i += 1
        if n % i == 0:
            ans += 1
            # Remove all factors of i from n
            while n % i == 0:
                n //= i
    
    # If there's any remaining prime factor greater than sqrt(n), it counts as one more divisor
    if n > 1:
        ans += 1
    
    return ans