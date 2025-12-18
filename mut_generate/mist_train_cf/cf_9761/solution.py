"""
QUESTION:
Create a function called median() that calculates the median of a list of numbers. The function should handle both even and odd length lists and return the median as a float for even length lists and as a single number for odd length lists. The function should be efficient and handle edge cases. The input list is not guaranteed to be sorted.
"""

def median(my_list):
    sorted_list = sorted(my_list)
    length = len(sorted_list)
    
    if length % 2 == 0:
        mid_index_1 = length // 2
        mid_index_2 = mid_index_1 - 1
        return (sorted_list[mid_index_1] + sorted_list[mid_index_2]) / 2
    else:
        return sorted_list[length // 2]