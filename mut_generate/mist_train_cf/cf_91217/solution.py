"""
QUESTION:
Design a function called `find_maximum` that takes an array of integers as input and returns the maximum value in the array. The array can contain duplicate elements and can have a maximum length of 10^6. The function should achieve a time complexity of O(n), where n is the length of the array.
"""

def findMaximum(array):
    max_value = array[0]
    
    for i in range(1, len(array)):  
        if array[i] > max_value:  
            max_value = array[i]  
    
    return max_value