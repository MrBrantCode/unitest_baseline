"""
QUESTION:
You are playing a game of Nim with a pile of n stones, where each player takes turns removing 1 to 3 stones. The player who removes the last stone wins. Write a function `canWinNim(n)` that determines if you can secure a win, assuming both you and your friend employ the best possible strategies. Return `true` if a win is feasible, and `false` otherwise. The input `n` satisfies `1 <= n <= 2^31 - 1`.
"""

def canWinNim(n):
    return n % 4 != 0