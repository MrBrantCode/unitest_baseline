"""
QUESTION:
Define a function `S(n)` that calculates the expected number of shuffles required to sort a deck of `n` cards in ascending order using a specific shuffling method. The function should not take any arguments other than `n`. The cards are shuffled and rearranged based on certain rules until they are sorted, and the expected number of shuffles is calculated. The function should return the expected number of shuffles required to sort the deck. Note that `S(1)` is defined as 0. The function should be able to handle large inputs, such as `n = 52`.
"""

def S(n):
    """
    Calculate the expected number of shuffles required to sort a deck of n cards in ascending order.

    Args:
    n (int): The number of cards in the deck.

    Returns:
    int: The expected number of shuffles required to sort the deck.
    """
    return n ** 2