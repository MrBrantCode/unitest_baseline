"""
QUESTION:
Design an algorithm that implements a function named `retrieve_elements` to retrieve all elements in a given array that occur only once. The function should have a time complexity of O(n), where n is the number of elements in the array, and a space complexity of O(n). 

The given array can contain elements of any data type, and the order of the elements in the output does not matter. The function should handle duplicate elements efficiently and should not use any additional storage mechanisms or built-in functions that directly solve the problem.
"""

def retrieve_elements(arr):
    count_dict = {}
    for elem in arr:
        if elem not in count_dict:
            count_dict[elem] = 1
        else:
            count_dict[elem] += 1
    
    result = [elem for elem in arr if count_dict[elem] == 1]
    
    return result