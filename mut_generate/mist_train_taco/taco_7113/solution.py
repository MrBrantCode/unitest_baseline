"""
QUESTION:
A Smith number is a composite number, the sum of whose digits is the sum of the digits of its prime factors obtained as a result of prime factorization (excluding ${1}$). The first few such numbers are ${4}$, $22$, $27$, $58$, $85$, ${94}$, and ${121}$.

Example: 

$378=2\times3\times3\times3\times7$ 

So, its prime factors are $2$, $3$, $3$, $3$, and $7$. 

The sum of its digits is $(3+7+8)=18$. 

The sum of the digits of its factors is $(2+3+3+3+7)=18$.  

Similarly, $4937775$ is a Smith number. 

$4937775=3\times5\times5\times65837$, and the sum of its digits is the same as the sum of the digits of its prime factors: $4+9+3+7+7+7+5=3+5+5+6+5+8+3+7=42$.

Task: 

Write a program to check whether a given integer is a Smith number.

Input Format

There will be only one line of input: $N$, the number which needs to be checked.

Constraints: 

$0<N<2,147,483,647$ (max value of an integer of the size of ${4}$ bytes)

Output Format

${1}$ if the number is a Smith number. 

${0}$ if the number is a not Smith number.  

Sample Input

378 

Sample Output

1

Explanation

Its prime factors are $2$, $3$, $3$, $3$, and $7$. 

The sum of its digits is $(3+7+8)=18$. 

The sum of the digits of its factors is $(2+3+3+3+7)=18$.
"""

import math

def findsum(a):
    """Helper function to find the sum of digits of a number."""
    r = 0
    for g in range(len(a)):
        r += int(a[g])
    return r

def is_smith_number(n):
    """Function to check if a given number is a Smith number."""
    if n < 2:
        return 0  # Smith numbers are composite numbers, so they must be greater than 1
    
    original_sum = findsum(str(n))
    prime_factors_sum = 0
    k = n
    
    for y in range(2, int(math.sqrt(k)) + 1):
        while k % y == 0:
            k //= y
            prime_factors_sum += findsum(str(y))
    
    if k != 1:
        prime_factors_sum += findsum(str(k))
    
    return 1 if original_sum == prime_factors_sum else 0