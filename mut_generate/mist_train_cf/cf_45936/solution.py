"""
QUESTION:
Write a function `min_stamps_needed` that takes in a list of unique stamp denominations and a total value, and returns the minimum number of stamps needed to reach the total value. The function should return `float('inf')` if it's impossible to reach the total value with the given stamp denominations.
"""

def min_stamps_needed(stamps, total):
    n = total + 1
    L = [0] + [float('inf')] * total
    
    for stamp in stamps:
        for i in range(stamp, n):
            L[i] = min(L[i], 1 + L[i - stamp])
    
    return L[total] if L[total] != float('inf') else float('inf')