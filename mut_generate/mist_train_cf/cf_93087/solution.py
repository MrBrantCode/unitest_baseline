"""
QUESTION:
Write a function `get_unique_elements(arr)` that retrieves all elements in a given array that occur only once. The function should have a time complexity of O(n), where n is the number of elements in the array, and should not use any built-in functions or libraries that directly solve the problem. The function can contain elements of any data type, including strings, floats, and objects, and the order of the elements in the output does not matter.
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