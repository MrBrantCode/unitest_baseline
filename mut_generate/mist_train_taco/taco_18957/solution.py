"""
QUESTION:
You are given a positive integer $n$.

Let $S(x)$ be sum of digits in base 10 representation of $x$, for example, $S(123) = 1 + 2 + 3 = 6$, $S(0) = 0$.

Your task is to find two integers $a, b$, such that $0 \leq a, b \leq n$, $a + b = n$ and $S(a) + S(b)$ is the largest possible among all such pairs.


-----Input-----

The only line of input contains an integer $n$ $(1 \leq n \leq 10^{12})$.


-----Output-----

Print largest $S(a) + S(b)$ among all pairs of integers $a, b$, such that $0 \leq a, b \leq n$ and $a + b = n$.


-----Examples-----
Input
35

Output
17

Input
10000000000

Output
91



-----Note-----

In the first example, you can choose, for example, $a = 17$ and $b = 18$, so that $S(17) + S(18) = 1 + 7 + 1 + 8 = 17$. It can be shown that it is impossible to get a larger answer.

In the second test example, you can choose, for example, $a = 5000000001$ and $b = 4999999999$, with $S(5000000001) + S(4999999999) = 91$. It can be shown that it is impossible to get a larger answer.
"""

def digisum(n):
    """Helper function to calculate the sum of digits of a number."""
    sum = 0
    while n != 0:
        sum += n % 10
        n = n // 10
    return sum

def give9(n):
    """Helper function to generate the largest number with all 9s that is less than or equal to n."""
    num9 = 0
    while n >= 10:
        num9 = num9 * 10 + 9
        n = n // 10
    return num9

def max_sum_of_digit_sums(n):
    """
    Function to find the largest possible sum of the digit sums of two integers a and b
    such that 0 ≤ a, b ≤ n and a + b = n.
    
    Parameters:
    n (int): The given positive integer.
    
    Returns:
    int: The largest possible sum of the digit sums of a and b.
    """
    a = give9(n)
    b = n - a
    return digisum(a) + digisum(b)