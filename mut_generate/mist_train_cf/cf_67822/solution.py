"""
QUESTION:
Write a function `accumulation` that takes a list of strings representing digits as input and returns a list of integers where each element is the cumulative sum of the integers represented by the input strings up to that point.
"""

def accumulation(lst):
    result = [int(lst[0])]
    for i in range(1, len(lst)):
        result.append(result[i-1] + int(lst[i]))
    return result