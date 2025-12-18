"""
QUESTION:
Write a function `kth_largest_distinct(numbers, k)` that finds the Kth largest distinct value in a list of numbers. The function should not use any built-in sorting functions or methods, handle cases where K is larger than the length of the list or the list contains duplicate values, and have a time complexity of O(N + KlogK), where N is the length of the list. The function should return None if K is larger than the length of the list, and it should be implemented recursively.
"""

def kth_largest_distinct(numbers, k):
    distinct_numbers = list(set(numbers))
    n = len(distinct_numbers)
    
    if k > n:
        return None
    
    pivot = distinct_numbers[-1]
    smaller = [x for x in distinct_numbers if x < pivot]
    equal = [x for x in distinct_numbers if x == pivot]
    larger = [x for x in distinct_numbers if x > pivot]
    
    m = len(larger)
    
    if k <= m:
        return kth_largest_distinct(larger, k)
    elif k > m + len(equal):
        return kth_largest_distinct(smaller, k - m - len(equal))
    else:
        return pivot