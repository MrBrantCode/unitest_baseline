"""
QUESTION:
Write a function cost(n) to calculate the minimum cost of the optimal prefix-free code of size n, where the cost of transmitting a '0' bit is one penny and the cost of transmitting a '1' bit is four pence. The cost of the optimal prefix-free code can be calculated using the following formulas: 

- If n is even, then cost(n) = 3 * cost(n/2) + 2 * (n mod 2) = 2.
- If n is odd, then cost(n) = 3 * cost((n-1)/2) + 4 * (n mod 2) = 4.
- cost(1) = 0.

Since the actual result for large values of n is quite large, return the result modulo 10^9.
"""

def cost(n):
    """
    Calculate the minimum cost of the optimal prefix-free code of size n.

    Args:
    n (int): The size of the optimal prefix-free code.

    Returns:
    int: The minimum cost of the optimal prefix-free code modulo 10^9.
    """
    cost_array = [0] * (n + 1)
    
    for i in range(2, n + 1):
        if (i % 2) == 0:
            cost_array[i] = 3 * cost_array[i // 2] + 2
        else:
            cost_array[i] = 3 * cost_array[i // 2] + 4
    
    return cost_array[n] % (10 ** 9)