"""
QUESTION:
You are tasked with creating a function `calculateTotalScore` that takes in two parameters: `hand`, a dictionary representing the letters available to the player, and `totalScore`, an integer representing the current total score. The function should check if the player's hand is empty and if so, print the total score. The function should use the `calculateHandlen` function, which returns the number of letters in the player's hand, to determine if the hand is empty.

The function should take a dictionary `hand` where 1 <= len(hand) <= 10^5, with lowercase letters as keys and their frequencies as values, and an integer `totalScore` where 0 <= totalScore <= 10^6. The function should return no value but print "Total score: X points." if the hand is empty, where X is the total score.
"""

def calculateTotalScore(hand: dict, totalScore: int) -> None:
    def calculateHandlen(hand: dict) -> int:
        return sum(hand.values())

    if calculateHandlen(hand) == 0:
        print('Total score: ' + str(totalScore) + ' points.')