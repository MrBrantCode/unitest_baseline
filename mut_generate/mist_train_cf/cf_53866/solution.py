"""
QUESTION:
Write a function `constituent_counter` that takes a two-dimensional array as input and returns a dictionary where each key is an element from the array and each value is the number of times that element occurred in the array. The function should work with arrays containing strings or numbers and should be able to handle arrays of varying sizes and structures.
"""

def constituent_counter(two_d_array):
    output = dict()
    for subarray in two_d_array:
        for item in subarray:
            if item in output:
                output[item] += 1
            else:
                output[item] = 1
    return output