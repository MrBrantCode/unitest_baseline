"""
QUESTION:
You are given a tetrahedron. Let's mark its vertices with letters A, B, C and D correspondingly.

<image>

An ant is standing in the vertex D of the tetrahedron. The ant is quite active and he wouldn't stay idle. At each moment of time he makes a step from one vertex to another one along some edge of the tetrahedron. The ant just can't stand on one place.

You do not have to do much to solve the problem: your task is to count the number of ways in which the ant can go from the initial vertex D to itself in exactly n steps. In other words, you are asked to find out the number of different cyclic paths with the length of n from vertex D to itself. As the number can be quite large, you should print it modulo 1000000007 (109 + 7). 

Input

The first line contains the only integer n (1 ≤ n ≤ 107) — the required length of the cyclic path.

Output

Print the only integer — the required number of ways modulo 1000000007 (109 + 7).

Examples

Input

2


Output

3


Input

4


Output

21

Note

The required paths in the first sample are: 

  * D - A - D
  * D - B - D
  * D - C - D
"""

def count_cyclic_paths(n: int) -> int:
    """
    Counts the number of ways an ant can go from vertex D to itself in exactly n steps on a tetrahedron.

    Parameters:
    n (int): The required length of the cyclic path.

    Returns:
    int: The number of ways modulo 1000000007 (10^9 + 7).
    """
    mod = 1000000007
    
    def fast_exp_pow(num: int, pw: int, mod: int) -> int:
        """
        Helper function to perform fast exponentiation with modulo.
        """
        num %= mod
        if pw == 1:
            return num
        evener = 1
        if pw % 2 == 1:
            evener = num
        return evener * (fast_exp_pow(num, pw // 2, mod) % mod) ** 2 % mod
    
    if n == 1:
        return 0
    
    x = (fast_exp_pow(3, n - 1, mod) + (-1) ** (n & 1) + mod) * 3 % mod
    y = 250000002
    
    return x * y % mod