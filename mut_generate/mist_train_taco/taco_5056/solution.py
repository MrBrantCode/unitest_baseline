"""
QUESTION:
I have the `par` value for each hole on a golf course and my stroke `score` on each hole. I have them stored as strings, because I wrote them down on a sheet of paper.  Right now, I'm using those strings to calculate my golf score by hand: take the difference between my actual `score` and the `par` of the hole, and add up the results for all 18 holes.

For example:
* If I took 7 shots on a hole where the par was 5, my score would be: 7 - 5 = 2
* If I got a hole-in-one where the par was 4, my score would be: 1 - 4 = -3.

Doing all this math by hand is really hard! Can you help make my life easier?


## Task Overview

Complete the function which accepts two strings and calculates the golf score of a game. Both strings will be of length 18, and each character in the string will be a number between 1 and 9 inclusive.
"""

def calculate_golf_score(par: str, score: str) -> int:
    """
    Calculate the total golf score based on the par values and actual scores for each hole.

    Parameters:
    - par (str): A string of length 18, where each character is the par value for a hole.
    - score (str): A string of length 18, where each character is the actual score for a hole.

    Returns:
    - int: The total golf score, calculated as the sum of the differences between the actual score and the par for each hole.
    """
    return sum((int(b) - int(a) for (a, b) in zip(par, score)))