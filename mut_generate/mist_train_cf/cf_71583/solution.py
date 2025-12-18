"""
QUESTION:
Write a function `maximumSwap(num)` that takes a non-negative integer `num` in the range [0, 10^8] and returns a tuple containing the maximum possible number that can be obtained by swapping two digits exactly once, along with the positions of the swapped digits. The positions are 0-indexed, and if no swap is needed, return the original number and (-1, -1).
"""

def maximumSwap(num):
    num = list(str(num))
    last = {int(x): i for i, x in enumerate(num)}

    for i, x in enumerate(num):
        for d in range(9, int(x), -1):
            if last.get(d, None) is not None and last[d] > i:
                num[i], num[last[d]] = num[last[d]], num[i]
                return int("".join(num)),(i,last[d])

    return int("".join(num)),(-1, -1)