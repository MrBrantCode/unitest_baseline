"""
QUESTION:
Snuke received a positive integer N from Takahashi. A positive integer m is called a favorite number when the following condition is satisfied:

* The quotient and remainder of N divided by m are equal, that is, \lfloor \frac{N}{m} \rfloor = N \bmod m holds.



Find all favorite numbers and print the sum of those.

Constraints

* All values in input are integers.
* 1 \leq N \leq 10^{12}

Input

Input is given from Standard Input in the following format:


N


Output

Print the answer.

Examples

Input

8


Output

10


Input

1000000000000


Output

2499686339916
"""

def sum_of_favorite_numbers(N: int) -> int:
    """
    Calculate the sum of all favorite numbers for a given positive integer N.
    
    A positive integer m is called a favorite number if the quotient and remainder of N divided by m are equal,
    i.e., \lfloor \frac{N}{m} \rfloor = N \bmod m.
    
    Parameters:
    - N (int): A positive integer.
    
    Returns:
    - int: The sum of all favorite numbers for the given N.
    """
    return sum([N // x - 1 for x in range(1, int(N ** 0.5) + 1) if N % x == 0 and N // x - 1 > x])