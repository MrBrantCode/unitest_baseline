"""
QUESTION:
Find the minimal number of marbles to insert to remove all the marbles on the table in a game of Marble Blast, given a row of marbles on the table and several marbles in hand. If it is impossible to remove all the marbles, return -1. 

Write a function `findMinStep(board, hand)` that takes in two parameters: `board`, the current state of the game as a string of characters representing the colors of the marbles, and `hand`, the marbles available to use as a string of characters representing the colors of the marbles.

Constraints: 
1 <= board.length <= 16
1 <= hand.length <= 5
Both input strings will be non-empty and only contain characters 'R','Y','B','G','W'. The initial row of marbles on the table won’t have any 4 or more consecutive marbles with the same color.
"""

def findMinStep(board, hand):
    from collections import Counter

    def dfs(board, hand_count):
        if not board: return 0
        res, i = float('inf'), 0
        while i < len(board):
            j = i + 1
            while j < len(board) and board[i] == board[j]: j += 1
            need = 3 - (j - i)
            if hand_count[board[i]] >= need:
                need = 0 if need < 0 else need
                hand_count[board[i]] -= need
                temp = dfs(board[:i] + board[j:], hand_count)
                if temp != -1: res = min(res, temp + need)
                hand_count[board[i]] += need
            i = j
        return -1 if res == float('inf') else res

    hand_count = Counter(hand)
    return dfs(board, hand_count)