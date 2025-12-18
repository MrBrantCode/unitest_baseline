"""
QUESTION:
Alex is transitioning from website design to coding and wants to sharpen his skills with CodeWars.  
He can do ten kata in an hour, but when he makes a mistake, he must do pushups. These pushups really tire poor Alex out, so every time he does them they take twice as long. His first set of redemption pushups takes 5 minutes. Create a function, `alexMistakes`, that takes two arguments: the number of kata he needs to complete, and the time in minutes he has to complete them. Your function should return how many mistakes Alex can afford to make.
"""

from math import log

def alex_mistakes(n, time):
    """
    Calculate the number of mistakes Alex can afford to make given the number of kata and the total time available.

    Parameters:
    n (int): The number of kata Alex needs to complete.
    time (int): The total time in minutes Alex has to complete the kata.

    Returns:
    int: The number of mistakes Alex can afford to make.
    """
    return int(log((time - n * 6) / 5 + 1, 2))