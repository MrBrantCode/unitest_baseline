"""
QUESTION:
Write a function `minFlips` that takes a string `target` of length `n` as input, where `n` is in the range `1 <= n <= 10^5` and each character in `target` is either '0' or '1', and returns the minimum number of flip operations required to achieve the configuration represented by `target` from an initial state of all '0's. A flip operation inverts all bulbs from the selected index to the end of the string.
"""

def minFlips(target: str) -> int:
    flips = 0
    prev = '0'
    for bulb in target:
        if bulb != prev:
            flips += 1
            prev = bulb
    return flips