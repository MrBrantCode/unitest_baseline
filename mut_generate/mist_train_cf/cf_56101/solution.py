"""
QUESTION:
Create a function `index_differences(arr1, arr2)` that takes two arrays `arr1` and `arr2` of distinct elements as input and returns the minimum sum of absolute differences between indices of the same elements in the two arrays. The function should have a time complexity of O(n), where n is the length of the arrays.
"""

def index_differences(arr1, arr2):
    pos1 = {value: index for index, value in enumerate(arr1)}
    pos2 = {value: index for index, value in enumerate(arr2)}
    
    common_values = set(pos1.keys()) & set(pos2.keys())
  
    return sum(abs(pos1[val] - pos2[val]) for val in common_values)