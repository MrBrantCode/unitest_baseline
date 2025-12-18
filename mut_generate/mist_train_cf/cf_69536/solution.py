"""
QUESTION:
Write a function `is_subset_sum` that determines if there is a subset of a given set of non-negative integers with a sum equal to a given target sum. The function should take three parameters: the set of non-negative integers, the number of elements in the set, and the target sum. The function should return a boolean value indicating whether such a subset exists. The set contains unique elements and is of length 1 to 200, with elements ranging from 0 to 1000. The target sum ranges from 0 to 1000.
"""

def is_subset_sum(set, n, sum): 
    if sum == 0:
        return True  
    if n == 0 and sum != 0:
        return False

    if set[n-1] > sum:
        return is_subset_sum(set, n-1, sum)

    return is_subset_sum(set, n-1, sum) or is_subset_sum(set, n-1, sum-set[n-1])