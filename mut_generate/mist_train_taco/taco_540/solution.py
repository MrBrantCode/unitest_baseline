"""
QUESTION:
For an integer n not less than 0, let us define f(n) as follows:
 - f(n) = 1 (if n < 2)
 - f(n) = n f(n-2) (if n \geq 2)
Given is an integer N. Find the number of trailing zeros in the decimal notation of f(N).

-----Constraints-----
 - 0 \leq N \leq 10^{18}

-----Input-----
Input is given from Standard Input in the following format:
N

-----Output-----
Print the number of trailing zeros in the decimal notation of f(N).

-----Sample Input-----
12

-----Sample Output-----
1

f(12) = 12 × 10 × 8 × 6 × 4 × 2 = 46080, which has one trailing zero.
"""

def count_trailing_zeros_of_f(n: int) -> int:
    """
    Calculate the number of trailing zeros in the decimal notation of f(n).

    Parameters:
    n (int): The integer input for which to calculate the number of trailing zeros in f(n).

    Returns:
    int: The number of trailing zeros in the decimal notation of f(n).
    """
    if n % 2 == 1:
        return 0
    
    A = 0
    add = 10
    while n >= add:
        A += n // add
        add *= 5
    
    return A