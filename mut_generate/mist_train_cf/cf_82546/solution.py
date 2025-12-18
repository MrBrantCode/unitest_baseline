"""
QUESTION:
Calculate the function F(n) that represents the total number of possible final outcomes in a tournament scenario with n teams, where each team competes against every other team twice and earns two points for a victory, one point for a draw, and no points for a defeat. Return F(n) modulo 10^9 + 7.

The function should follow these rules: F(0) = 1, and for i from 1 to n, F(i) is calculated based on F(i-1) and the number of possible outcomes for the matches between the i-th team and the previous teams.
"""

def number_of_outcomes(n):
    """
    Calculate the total number of possible final outcomes in a tournament scenario with n teams.
    
    Parameters:
    n (int): The number of teams.
    
    Returns:
    int: The total number of possible final outcomes modulo 10^9 + 7.
    """
    mod = 10**9 + 7

    def choose(n, k):
        """
        Calculate binomial coefficients using Pascal's triangle approach.
        
        Parameters:
        n (int): The total number of items.
        k (int): The number of items to choose.
        
        Returns:
        int: The binomial coefficient modulo 10^9 + 7.
        """
        if k > n:
            return 0
        if k > n // 2:
            k = n - k
        x = 1
        y = 1
        for i in range(1, k + 1):
            x = (x * (n + 1 - i)) % mod
            y = (y * i) % mod
        return (x * pow(y, mod - 2, mod)) % mod

    F = [0] * (n + 1)
    F[0] = 1

    for i in range(1, n + 1):
        for j in range(i * (i - 1) // 2, -1, -1):
            if F[i] == 0:
                F[i] = F[i - 1]
            else:
                F[i] = (F[i] + choose(i * (i - 1) // 2, j) * (F[i - 1] ** ((i * (i - 1)) // 2 - j) % mod) * ((2 * i - 1) ** j) % mod) % mod

    return F[n]