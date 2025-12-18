"""
QUESTION:
Rhezo likes numbers of the form A^B. But computing A^B, for any 2 numbers A and B is a hard task for him. He would like you to help him out in this.

Input:
First line of input contains a single integer A. Second line contains the integer B.

Output:
Help Rhezo find A^B. As this number can be large, print it modulo 10^9+7.

Constraints:
 1 ≤ A ≤ 10^9  
 1 ≤ B ≤ 10^{10^5} 

SAMPLE INPUT
4
3

SAMPLE OUTPUT
64
"""

def compute_power_modulo(A: int, B: int, mod: int = 1000000007) -> int:
    """
    Computes the power of A raised to B modulo mod.

    Parameters:
    A (int): The base number.
    B (int): The exponent.
    mod (int): The modulo value (default is 10^9 + 7).

    Returns:
    int: The result of A^B % mod.
    """
    return pow(A, B, mod)