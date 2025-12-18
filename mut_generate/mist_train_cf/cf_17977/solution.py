"""
QUESTION:
Create a function named `remove_duplicates` that takes an array of integers as input and returns an array of integers. The output array should contain all elements from the original array except for the duplicates. The function must achieve this in a time complexity of O(n), where n is the length of the input array, without using any built-in functions or libraries.
"""

def remove_duplicates(arr):
    count_dict = {}
    
    for num in arr:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    result = []
    
    for num in arr:
        if count_dict[num] == 1:
            result.append(num)
    
    return result