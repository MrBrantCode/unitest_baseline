"""
QUESTION:
Write a function `PredictTheWinner(nums)` that predicts whether player 1 is the winner in a game where two players take turns picking numbers from either end of the array. Each player can skip their turn up to 2 times. The player with the maximum score wins, and if the scores are equal, player 1 is still the winner. The function should return True if player 1 is the winner and False otherwise. The array `nums` contains non-negative integers, has a length between 1 and 20, and each integer does not exceed 10,000,000.
"""

import sys

def PredictTheWinner(nums):
    def Score(arr, player1, player2, turn, p1_skipped, p2_skipped):
        if len(arr) == 0 or (p1_skipped == 2 and p2_skipped == 2):
            return player1 >= player2
        score = sys.maxsize if turn else -sys.maxsize
        for i in range(2):
            if i == 0:
                new_arr = arr[1:]
                new_score = Score(new_arr, player1 + arr[0] * turn, player2 + arr[0] * (1 - turn), 1 - turn, p1_skipped + turn, p2_skipped + (1 - turn))
            else:
                new_arr = arr[:-1]
                new_score = Score(new_arr, player1 + arr[-1] * turn, player2 + arr[-1] * (1 - turn), 1 - turn, p1_skipped + turn, p2_skipped + (1 - turn))
            if turn:
                score = min(score, new_score)
            else:
                score = max(score, new_score)
            if p1_skipped < 2 and turn == 0:
                score = max(score, Score(arr, player1, player2, 1 - turn, p1_skipped + 1, p2_skipped))
            if p2_skipped < 2 and turn == 1:
                score = min(score, Score(arr, player1, player2, 1 - turn, p1_skipped, p2_skipped + 1))
        return score

    if len(nums) == 0:
        return True
    return Score(nums, 0, 0, 0, 0, 0)