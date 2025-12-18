"""
QUESTION:
Find the function `sum_of_losing_configurations(n)` that calculates the sum of all losing configurations in a four-pile stone game where the piles are numbered from 0 to n and the stones in the piles are numbered from 0 to n. In a losing configuration, the bitwise XOR of the four piles is 0, and the number of stones removed from each pile is the same if stones are removed from multiple piles. The function should return the sum of the total number of stones in all losing configurations.
"""

def sum_of_losing_configurations(n):
    """
    Calculate the sum of all losing configurations in a four-pile stone game.
    
    Parameters:
    n (int): The maximum number of stones in each pile.
    
    Returns:
    int: The sum of the total number of stones in all losing configurations.
    """
    total = 0

    for j1 in range(n + 1):
        for j2 in range(j1, n + 1):
            nim_sum = j1 ^ j2
            for j3 in range(j2, nim_sum ^ j1 + 1):
                j4 = nim_sum ^ j3
                if j4 >= j3 and j4 <= n:
                    total += j1 + j2 + j3 + j4

    return total