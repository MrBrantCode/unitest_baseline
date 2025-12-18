"""
QUESTION:
In this Kata, you will be given a number and your task will be to rearrange the number so that it is divisible by `25`, but without leading zeros. Return the minimum number of digit moves that are needed to make this possible. If impossible, return `-1` ( `Nothing` in Haskell ).

For example:

More examples in test cases.

Good luck!
"""

def min_moves_to_divisible_by_25(n: int) -> int:
    moves = []
    for (a, b) in ['25', '75', '50', '00']:
        s = str(n)[::-1]
        x = s.find(a)
        y = s.find(b, x + 1 if a == '0' else 0)
        if x == -1 or y == -1:
            continue
        moves.append(x + y - (x > y) - (a == b))
        s = s.replace(a, '', 1).replace(b, '', 1)
        l = len(s.rstrip('0'))
        if l:
            moves[-1] = moves[-1] + (len(s) - l)
        elif s:
            moves.pop()
    return min(moves, default=-1)