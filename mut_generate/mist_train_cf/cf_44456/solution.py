"""
QUESTION:
Create a function `find_larger_elements(lst, k)` that takes a list `lst` and a number `k` as input. The function should return a tuple containing the count of elements in `lst` that are larger than `k` and a list of their corresponding indices. The function should handle cases where `lst` contains both integer and string numbers, and string numbers should be converted to integers before comparison.
"""

def find_larger_elements(lst, k):
    # Stores the count of elements larger than k and their indices
    count = 0
    indices = []
    
    for i, item in enumerate(lst):
        # Casts the item to int, covers both cases of int or str
        item = int(item)
        
        if item > k:
            count += 1
            indices.append(i)
    
    return count, indices