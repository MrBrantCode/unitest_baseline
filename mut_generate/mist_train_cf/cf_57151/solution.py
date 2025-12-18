"""
QUESTION:
Compute the function L(N,K), representing the total number of arrangements for K non-attacking Sliders on an N x N cylindrical chess-board, where a Slider can move one square either to the left or right and the left and right edges are interconnected. The function should return L(N,K) modulo (10^7+19)^2.
"""

def entance(n, k, modulo=(10**7+19)**2):
    """
    Compute the total number of arrangements for k non-attacking Sliders 
    on an n x n cylindrical chess-board.

    Args:
        n (int): The size of the cylindrical chess board.
        k (int): The number of Sliders.
        modulo (int): The modulo value. Defaults to (10^7+19)^2.

    Returns:
        int: The total number of arrangements modulo (10^7+19)^2.
    """

    def binomial_coefficient(n, k, modulo):
        if k == 0 or k == n:
            return 1
        else:
            return (binomial_coefficient(n-1, k-1, modulo) + binomial_coefficient(n-1, k, modulo)) % modulo

    return binomial_coefficient(n, k, modulo)