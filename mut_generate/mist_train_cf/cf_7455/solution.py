"""
QUESTION:
Design a function named `retrieve_elements` to retrieve all elements in a given array that occur only once. The function should have a time complexity of O(n) where n is the number of elements in the array. The given array can contain elements of any data type, including integers, strings, floats, and objects. The function should not use any built-in functions or libraries that directly solve the problem, and it should use constant space complexity.
"""

def retrieve_elements(arr):
    count_dict = {}
    for elem in arr:
        if elem not in count_dict:
            count_dict[elem] = 1
        else:
            count_dict[elem] += 1
    
    result = []
    for elem in arr:
        if count_dict[elem] == 1:
            result.append(elem)
    
    return result