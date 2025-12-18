"""
QUESTION:
Design a function `find_maximum(array)` that finds the maximum value in a given array. The array can have a maximum length of 10^6 and may contain duplicate elements. The time complexity of the solution should be O(n), where n is the length of the array.
"""

def find_maximum(array):
    max_value = array[0]  # initialize max_value with the first element of the array
    
    for i in range(1, len(array)):  # start loop from second element
        if array[i] > max_value:  # if current element is greater than max_value
            max_value = array[i]  # update max_value
    
    return max_value