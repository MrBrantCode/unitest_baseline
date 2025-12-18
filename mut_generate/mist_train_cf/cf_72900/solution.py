"""
QUESTION:
Write a function named `catalan_numbers` that calculates Catalan numbers for a given ordinal number or a range of ordinal numbers. The function should handle edge cases and incorrect inputs, and use memoization to improve performance for large inputs. The function should accept a single integer or a tuple representing a range of ordinal numbers. For negative ordinal numbers, the function should return 0. The function should return a single integer for a single ordinal number input, and a list of integers for a range of ordinal numbers input. The function should not cause a stack overflow for large inputs.
"""

from functools import lru_cache

@lru_cache(maxsize=None)
def catalan_number(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    catalan = [0 for _ in range(n+1)]
    catalan[0] = catalan[1] = 1
    for i in range(2, n+1):
        for j in range(i):
            catalan[i] += catalan[j] * catalan[i-j-1]
    return catalan[n]

def catalan_numbers(arg):
    if isinstance(arg, int):
        return catalan_number(arg)
    elif isinstance(arg, tuple) and len(arg) == 2:
        start, end = arg
        if not all(isinstance(x, int) for x in [start, end]):
            print("ERROR: Both range specifications must be integers.")
        elif start > end:
            print("ERROR: Start of range must be less than end.")
            return []
        else:
            return [catalan_number(n) for n in range(start, end+1)]
    else:
        print("ERROR: Argument must be a single integer or a range.")
        return []