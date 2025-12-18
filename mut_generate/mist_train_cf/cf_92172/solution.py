"""
QUESTION:
Write a function `check_subset` that checks whether `subsetArray` is a subset of `supersetArray` and returns a boolean value indicating whether it is a subset. Additionally, write a function `count_occurrences` that returns a dictionary containing the count of occurrences of each element in `subsetArray` within `supersetArray`. The function should handle negative integers and duplicate elements in both arrays.
"""

def entance(subsetArray, supersetArray):
    subset_dict = {}
    
    for num in subsetArray:
        if num in subset_dict:
            subset_dict[num] += 1
        else:
            subset_dict[num] = 1
    
    for num in subset_dict:
        if subset_dict[num] > supersetArray.count(num):
            return False
    
    occurrences_dict = {}
    
    for num in subset_dict:
        occurrences_dict[num] = supersetArray.count(num)
    
    return True, occurrences_dict