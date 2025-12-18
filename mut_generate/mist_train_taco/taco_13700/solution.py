"""
QUESTION:
The following problem is well-known: given integers n and m, calculate $2^{n} \operatorname{mod} m$, 

where 2^{n} = 2·2·...·2 (n factors), and $x \operatorname{mod} y$ denotes the remainder of division of x by y.

You are asked to solve the "reverse" problem. Given integers n and m, calculate $m \operatorname{mod} 2^{n}$. 


-----Input-----

The first line contains a single integer n (1 ≤ n ≤ 10^8).

The second line contains a single integer m (1 ≤ m ≤ 10^8).


-----Output-----

Output a single integer — the value of $m \operatorname{mod} 2^{n}$.


-----Examples-----
Input
4
42

Output
10

Input
1
58

Output
0

Input
98765432
23456789

Output
23456789



-----Note-----

In the first example, the remainder of division of 42 by 2^4 = 16 is equal to 10.

In the second example, 58 is divisible by 2^1 = 2 without remainder, and the answer is 0.
"""

def calculate_mod_of_power_of_two(n: int, m: int) -> int:
    """
    Calculate the value of m modulo 2^n.

    Parameters:
    n (int): The exponent for the power of two.
    m (int): The integer to be divided.

    Returns:
    int: The remainder of m divided by 2^n.
    """
    if n > 26:
        return m
    two_n = 2 ** n
    return m % two_n