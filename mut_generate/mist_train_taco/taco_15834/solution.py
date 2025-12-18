"""
QUESTION:
You're given an integer $n$. For every integer $i$ from $2$ to $n$, assign a positive integer $a_i$ such that the following conditions hold:  For any pair of integers $(i,j)$, if $i$ and $j$ are coprime, $a_i \neq a_j$.  The maximal value of all $a_i$ should be minimized (that is, as small as possible). 

A pair of integers is called coprime if their greatest common divisor is $1$.


-----Input-----

The only line contains the integer $n$ ($2 \le n \le 10^5$).


-----Output-----

Print $n-1$ integers, $a_2$, $a_3$, $\ldots$, $a_n$ ($1 \leq a_i \leq n$). 

If there are multiple solutions, print any of them.


-----Examples-----
Input
4

Output
1 2 1 
Input
3

Output
2 1


-----Note-----

In the first example, notice that $3$ and $4$ are coprime, so $a_3 \neq a_4$. Also, notice that $a=[1,2,3]$ satisfies the first condition, but it's not a correct answer because its maximal value is $3$.
"""

import math

def assign_coprime_values(n):
    """
    Assigns positive integers to each integer from 2 to n such that for any pair of integers (i, j),
    if i and j are coprime, a_i != a_j. The maximal value of all a_i should be minimized.

    Parameters:
    n (int): The upper limit of the range (2 to n).

    Returns:
    list: A list of integers representing the values a_2, a_3, ..., a_n.
    """
    arr = [1, 2] + [0] * (n - 2)

    def isprime(x):
        y = int(math.sqrt(x)) + 1
        for i in range(2, y):
            if x % i == 0:
                return i
        return x

    p = 3
    for i in range(4, n + 1):
        x = isprime(i)
        if x == i:
            arr[i - 2] = p
            p += 1
        else:
            arr[i - 2] = arr[x - 2]

    return arr[:n - 1]