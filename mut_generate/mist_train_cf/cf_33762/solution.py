"""
QUESTION:
Write a function `calculateClearedValue(n: int) -> int` that takes an integer `n` as input, where `cleared` is initially 0 and incremented by 1 in each iteration. The function should return the value of `cleared` after `n` iterations.
"""

def calculateClearedValue(n: int) -> int:
    cleared = 0
    for _ in range(n):
        cleared += 1
    return cleared