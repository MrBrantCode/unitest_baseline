"""
QUESTION:
Write a function `third_largest` that identifies the third largest unique number in a multidimensional array. The function should handle negative numbers, return 'None' if the array has less than three unique numbers, and ignore non-numeric values. The function should be able to handle arrays of varying depths and not use any built-in sorting functions. The time complexity should be O(n log n) or better.
"""

def third_largest(arr):
    nums = [x for x in set(flatten(arr)) if isinstance(x, (int, float))]
    first = second = third = float('-inf')
    for i in nums:
        if i > first:
            first, second, third = i, first, second
        elif first > i > second:
            second, third = i, second
        elif second > i > third:
            third = i
    return third if third != float('-inf') else None

def flatten(arr):
    for i in arr:
        if isinstance(i, list):
            yield from flatten(i)
        else:
            yield i