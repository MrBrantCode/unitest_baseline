"""
QUESTION:
Write a function named `find_min_disparity` that takes a multidimensional array `arr` as input. The function should find the smallest disparity between any pair of elements within the array. It should also return the pair of elements that have the smallest disparity. The function should handle edge cases such as an empty array, an array with only one element, non-numeric elements, and duplicate elements. If the array is empty or contains only one element, the function should return a suitable message. If the array contains non-numeric elements, the function should ignore them and continue with the numeric ones. If the array contains duplicate elements, the function should return the pair of duplicate elements as the pair with the smallest disparity.
"""

def find_min_disparity(arr):
    if not isinstance(arr, list):
        return "Provided argument is not a list"

    flat_list = flatten(arr)
    
    if not flat_list:
        return "Empty Array Provided"
    if len(flat_list) == 1:
        return "Single element in the array"
    if len(set(flat_list)) == 1:
        return 0, (flat_list[0], flat_list[0])

    numeric_list = [i for i in flat_list if isinstance(i, (int, float))]
    numeric_list.sort()

    min_disparity = float('inf')
    pair = ()
    
    for i in range(len(numeric_list)-1):
        if abs(numeric_list[i]-numeric_list[i+1]) < min_disparity:
            min_disparity = abs(numeric_list[i]-numeric_list[i+1])
            pair = (numeric_list[i], numeric_list[i+1])
            
    return min_disparity, pair

def flatten(lst):
    result = []
    for i in lst:
        if isinstance(i, list): 
            result.extend(flatten(i))
        else:
            result.append(i)
    return result