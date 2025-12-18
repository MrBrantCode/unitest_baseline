"""
QUESTION:
Given an integer range [A,B],  

What’s the probability to get a 1-bit if we first randomly choose a number x in the range and then randomly choose a bit from x?  
What’s the expected number of bit 1s if we randomly choose a number x in the range?  

Input Format 

The first line of input is the number of test cases $\mathbf{T}$ 

Each test cases is a line contains 2 integers $\mbox{A}$ and $\mbox{B}$ separated by a space. 

Output Format 

For each test case output a line containing 2 float numbers separated by a space. The first one is the probability and the second one is the expected number. You should output the number accurate to 5 fractional digits. 

Constraints 

$1\leq T\leq200$ 

$1\leq A\leq B\leq10^{10}$  

Sample Input

1
2 4

Sample Output

0.61111 1.33333

Explanation 

(10)  (11)  (100) 

(1) So we got a one in $\frac{1}{3}\times\frac{1}{2}+\frac{1}{3}\times\frac{1}{1}+\frac{1}{3}\times\frac{1}{3}=\frac{11}{18}$ 

(2) The expected 1 we have is : $1\times\frac{1}{3}+2\times\frac{1}{3}+1\times\frac{1}{3}=\frac{4}{3}$
"""

from functools import lru_cache

@lru_cache(maxsize=None)
def s1(n):
    if n < 3:
        return n
    if n % 2 == 0:
        return s1(n // 2) + s1(n // 2 - 1) + n // 2
    return 2 * s1(n // 2) + n // 2 + 1

def s2(n):
    res = 0
    for i in range(1, 40):
        if 2 ** i > n:
            return res + (s1(n) - s1(2 ** (i - 1) - 1)) / i
        res += (1 + 1 / i) / 2 * 2 ** (i - 1)

def calculate_bit_statistics(A, B):
    """
    Calculate the probability of getting a 1-bit and the expected number of bit 1s
    for a randomly chosen number in the range [A, B].

    Parameters:
    A (int): The lower bound of the range.
    B (int): The upper bound of the range.

    Returns:
    tuple: A tuple containing two float numbers:
           - The probability of getting a 1-bit.
           - The expected number of bit 1s.
    """
    ans1 = (s2(B) - s2(A - 1)) / (B - A + 1)
    ans2 = (s1(B) - s1(A - 1)) / (B - A + 1)
    return round(ans1, 5), round(ans2, 5)