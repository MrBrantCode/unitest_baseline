"""
QUESTION:
Design a function `trifib(n: int)` that calculates the nth element of the TriFib sequence, where the sequence is defined as: trifib(0) == 0, trifib(1) == 0, trifib(2) == 1, and trifib(n) == trifib(n-1) + trifib(n-2) + trifib(n-3) + trifib(n-4). The function should use dynamic programming techniques and should be able to handle inputs up to 10,000.
"""

def trifib(n: int) -> int:
    if n < 0:
        return None
    # initialize trifib_arr with base cases 
    trifib_arr = [0, 0, 1]
    while len(trifib_arr) <= n:
        # compute the next trifib number by adding 3 previous numbers
        trifib_arr.append(sum(trifib_arr[-3:]))
    return trifib_arr[n]