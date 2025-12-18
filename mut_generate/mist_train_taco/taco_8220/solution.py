"""
QUESTION:
Given N integers A_1, ..., A_N, compute A_1 \times ... \times A_N.
However, if the result exceeds 10^{18}, print -1 instead.

-----Constraints-----
 - 2 \leq N \leq 10^5
 - 0 \leq A_i \leq 10^{18}
 - All values in input are integers.

-----Input-----
Input is given from Standard Input in the following format:
N
A_1 ... A_N

-----Output-----
Print the value A_1 \times ... \times A_N as an integer, or -1 if the value exceeds 10^{18}.

-----Sample Input-----
2
1000000000 1000000000

-----Sample Output-----
1000000000000000000

We have 1000000000 \times 1000000000 = 1000000000000000000.
"""

def compute_product_or_overflow(A: list) -> int:
    """
    Compute the product of all integers in the list A.
    If the product exceeds 10^18, return -1.

    Parameters:
    A (list): A list of integers.

    Returns:
    int: The product of the integers in A, or -1 if the product exceeds 10^18.
    """
    P = 10 ** 18
    if 0 in A:
        return 0
    
    product = 1
    for a in A:
        product *= a
        if product > P:
            return -1
    
    return product