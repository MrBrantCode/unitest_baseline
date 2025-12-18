"""
QUESTION:
Write a function `find_kth_smallest` that selects the kth smallest item from a list. The function takes a list of numbers and an integer k as input, where 1 ≤ k ≤ length of the list. The function should return the kth smallest number in the list. Implement the function with a time complexity of O(n) and a space complexity of O(1).
"""

def find_kth_smallest(lst, k):
    if k < 1 or k > len(lst):
        return None
    
    min_val = min(lst)
    max_val = max(lst)
    
    while min_val <= max_val:
        pivot = min_val + (max_val - min_val) // 2
        count_smaller = 0
        count_equal = 0
        
        for num in lst:
            if num < pivot:
                count_smaller += 1
            elif num == pivot:
                count_equal += 1
        
        if k <= count_smaller:
            max_val = pivot - 1
        elif k > count_smaller + count_equal:
            min_val = pivot + 1
        else:
            return pivot
    
    return None