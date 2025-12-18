"""
QUESTION:
The [Sharkovsky's Theorem](https://en.wikipedia.org/wiki/Sharkovskii%27s_theorem) involves the following ordering of the natural numbers:
```math
3≺5≺7≺9≺ ...\\
≺2·3≺2·5≺2·7≺2·9≺...\\
≺2^n·3≺2^n·5≺2^n·7≺2^n·9≺...\\
≺2^{(n+1)}·3≺2^{(n+1)}·5≺2^{(n+1)}·7≺2^{(n+1)}·9≺...\\
≺2^n≺2^{(n-1)}≺...\\
≺4≺2≺1\\
```
 
Your task is to complete the function which returns `true` if `$a≺b$` according to this ordering, and `false` otherwise.
 
You may assume both `$a$` and `$b$` are non-zero positive integers.
"""

def is_precedence_sharkovsky(a: int, b: int) -> bool:
    """
    Determines if 'a' precedes 'b' according to Sharkovsky's ordering.

    Parameters:
    a (int): The first non-zero positive integer.
    b (int): The second non-zero positive integer.

    Returns:
    bool: True if 'a' precedes 'b' in Sharkovsky's ordering, False otherwise.
    """
    
    def f(n: int, p: int = 0) -> tuple:
        """
        Helper function to compute the Sharkovsky ordering key for a given number.

        Parameters:
        n (int): The number to compute the key for.
        p (int): The initial power of 2 (default is 0).

        Returns:
        tuple: A tuple representing the Sharkovsky ordering key.
        """
        while n % 2 == 0:
            n >>= 1
            p += 1
        return (n == 1, p * (-1) ** (n == 1), n)
    
    return f(a) < f(b)