"""
QUESTION:
Write a function `rearrange_even_nums` that takes an array of integers as input and returns a boolean value. The function should rearrange the array such that even-indexed elements are less than or equal to the next element and odd-indexed elements are greater than or equal to the next element. The function is allowed to perform at most two swaps of exactly two elements each. If the array can be rearranged to meet the condition with at most two swaps, the function should return True. Otherwise, it should return False. The function should also handle the case where the input array is empty, in which case it should return True.
"""

def rearrange_even_nums(array):
    if not array:  
        return True

    max_num = max(array)
    max_idx = array.index(max_num)
    array[-1], array[max_idx] = array[max_idx], array[-1]

    pair_swaps_count = 0
    for i, num in enumerate(array[:-1]):
        if num % 2 == 1:  
            if i % 2 == 0:  
                pair_swaps_count += 1
                if pair_swaps_count > 2:  
                    return False
                array[i], array[i+1] = array[i+1], array[i]
        else:  
            if i % 2 == 1:  
                pair_swaps_count += 1
                if pair_swaps_count > 2:  
                    return False
                array[i], array[i+1] = array[i+1], array[i]

    return all(array[i] <= array[i+1] for i in range(len(array)-1))