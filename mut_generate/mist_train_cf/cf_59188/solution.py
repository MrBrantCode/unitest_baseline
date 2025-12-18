"""
QUESTION:
Given a list of non-negative integers `nums`, write a function `aliceWins` that returns `True` if Alice wins the chalkboard addition game and `False` otherwise. The game is played by two players, Alice and Bob, who take turns erasing exactly one number from the chalkboard, with Alice starting first. The game ends when the sum of all elements on the chalkboard becomes 0, resulting in a loss for the player who caused it. The function must assume both players play optimally. The input `nums` has a length of 1 to 1000, and each element is an integer between 0 and 2^16.
"""

def aliceWins(nums):
    xor_value = 0
    for i in nums:
        xor_value ^= i
    return xor_value != 0