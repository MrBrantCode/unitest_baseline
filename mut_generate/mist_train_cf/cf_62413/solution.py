"""
QUESTION:
Create a function named `reverse_and_sort` that takes two parameters: an array and a position. The function should reverse the array up to the specified position and arrange the remaining segment in ascending order. It should handle edge cases such as an empty array, an array with a single element, or a position that exceeds the array's boundaries. The function should also be able to handle arrays containing duplicate elements, negative integers, floating point numbers, and elements of different data types (integers, floating point numbers, and strings). In the sorted segment, string elements should be sorted in lexicographical order and placed after the numeric elements. The function should preserve the initial sequence of duplicate elements after sorting.
"""

def reverse_and_sort(arr, pos):
    len_arr = len(arr)
    if len_arr == 0:   #edge case for empty array
        return []
    elif len_arr == 1:    #edge case for single element
        return arr
    else:
        #edge case for position that exceeds the array's boundaries
        pos = min(pos, len_arr)  
        arr[:pos] = arr[:pos][::-1]   
        
        num_list = [i for i in arr[pos:] if isinstance(i, (int, float))]
        str_list = [i for i in arr[pos:] if isinstance(i, str)]
        num_list.sort()        # Sorting numbers only
        str_list.sort()        # Sorting strings only
        arr[pos:] = num_list + str_list    # Putting back together

    return arr