"""
QUESTION:
Write a function `get_unique_elements` that takes an array as input and returns all elements that occur only once. The function should have a time complexity of O(n) and constant space complexity, where n is the number of elements in the array. The input array can contain elements of any data type, and the order of the output does not matter.
"""

def get_unique_elements(arr):
    count_dict = {}
    for num in arr:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    result = []
    for key, value in count_dict.items():
        if value == 1:
            result.append(key)
    
    return result