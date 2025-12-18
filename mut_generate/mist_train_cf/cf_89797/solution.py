"""
QUESTION:
Create a function named `multiply_array` that takes two inputs: an array of positive integers (`arr`) with a length between 1 and 100, and a positive integer (`num`) between 1 and 10. The function should return a new array where each element of the input array is multiplied by the given number, with the resulting array containing only unique elements in the original order.
"""

def multiply_array(arr, num):
    multiplied_arr = []
    multiplied_set = set()
    for element in arr:
        multiplied_element = element * num
        if multiplied_element not in multiplied_set:
            multiplied_arr.append(multiplied_element)
            multiplied_set.add(multiplied_element)
    return multiplied_arr