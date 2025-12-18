"""
QUESTION:
Given two integer arrays `aliceValues` and `bobValues` of length `n`, where `aliceValues[i]` and `bobValues[i]` represent how Alice and Bob value the `i-th` stone, determine the result of a game where players take turns removing a stone from a pile and receiving points based on the stone's value. The game ends when all stones are chosen, and the player with the most points wins. If both players have the same amount of points, the game results in a draw.

The function `stoneGameVI(aliceValues, bobValues)` should return `1` if Alice wins, `-1` if Bob wins, and `0` if the game results in a draw.

Constraints: `n == aliceValues.length == bobValues.length`, `1 <= n <= 10^5`, `1 <= aliceValues[i], bobValues[i] <= 100`, and the index of the chosen stone must be a prime number or 1.
"""

from typing import List

def stoneGameVI(aliceValues: List[int], bobValues: List[int]) -> int:
    n = len(aliceValues)
    total = []
    for i in range(n):
        total.append((aliceValues[i] + bobValues[i], aliceValues[i], bobValues[i]))
        
    total.sort(reverse=True)
    aliceScore = bobScore = 0
    for i in range(n):
        if i%2==0: 
            aliceScore += total[i][1]
        else: 
            bobScore += total[i][2] 

    if aliceScore > bobScore:
        return 1
    elif aliceScore < bobScore:
        return -1
    else: 
        return 0