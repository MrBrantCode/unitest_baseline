"""
QUESTION:
Given a list of integers, write a function `repeat_and_reverse` that returns a new list where each element is repeated twice and the order of the repeated elements is reversed compared to the original list. The returned list should be sorted in ascending order. 

The input list will have a length between 2 and 1000 (inclusive), and will contain unique integers between -1000 and 1000 (inclusive). The solution should have a time complexity of O(n log n), where n is the length of the list.
"""

def repeat_and_reverse(arr):
    arr.sort()
    result = []
    for num in arr:
        result.append(num)
        result.append(num)
        result[-2], result[-1] = result[-1], result[-2]
    return result