"""
QUESTION:
Design a function called `combine_collections` that takes two lists of integers A and B as input, combines them into one list, removes duplicates, and sorts the resulting list in ascending order. 

The function should not use built-in functions for merging or sorting the list, and it should handle large integers (up to 10^9) and a total combined length of the input lists not exceeding 10^7. The time complexity should not exceed O(n log(n)).
"""

def combine_collections(A, B):
    def merge(left, right):
        if not left:
            return right
        if not right:
            return left
        if left[0] < right[0]:
            return [left[0]] + merge(left[1:], right)
        return [right[0]] + merge(left, right[1:])

    def mergesort(lst):
        if len(lst) <= 1:
            return lst
        mid = len(lst) // 2
        left = mergesort(lst[:mid])
        right = mergesort(lst[mid:])
        return merge(left, right)

    collection = list(set(A + B))
    if len(collection) > 10**7:
        raise Exception('Combined size of the collections is too large.')
    for num in collection:
        if abs(num) > 10**9:
            raise Exception('Number is too large.')
    return mergesort(collection)