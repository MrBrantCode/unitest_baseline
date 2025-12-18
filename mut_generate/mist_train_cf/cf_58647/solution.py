"""
QUESTION:
Define a function S that maps an integer n (n ≥ 3) to the count of functions T that map the set of sequences of n elements from {false, true} to {false, true} such that for every sequence x, the logical AND operation between T(x) and T(f(x)) results in false, where f(x) is defined as the sequence obtained by shifting the elements of x one position to the left and the last element being the logical AND of the first and the logical XOR of the second and third elements of x. Compute S(20) modulo 1,001,001,011.
"""

def S(n, mod=1001001011):
    """
    Compute S(n), the count of functions T that map the set of sequences of n elements from {false, true} to {false, true} 
    such that for every sequence x, the logical AND operation between T(x) and T(f(x)) results in false.

    Args:
    n (int): The number of elements in the sequence.
    mod (int): The modulo value. Default is 1001001011.

    Returns:
    int: S(n) modulo mod.
    """
    return (pow(2, pow(2, n, mod - 1), mod) - pow(2, pow(2, n - 1, mod - 1), mod)) % mod