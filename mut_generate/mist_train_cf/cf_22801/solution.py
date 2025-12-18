"""
QUESTION:
Implement a function `max_sum_k_elements(arr, k)` that selects k non-consecutive and non-repeating elements from an array `arr` to maximize their sum. The function should have a time complexity of O(n), where n is the length of `arr`. The function should also handle arrays containing negative numbers.
"""

def max_sum_k_elements(arr, k):
    n = len(arr)
    
    if n == 0 or k == 0:
        return 0
    
    if n == 1:
        return arr[0] if k == 1 else 0
    
    include = max(0, arr[0])
    exclude = 0
    
    for i in range(1, n):
        new_include = max(exclude + max(0, arr[i]), include)
        exclude = max(include, exclude)
        include = new_include
    
    return max(include, exclude)