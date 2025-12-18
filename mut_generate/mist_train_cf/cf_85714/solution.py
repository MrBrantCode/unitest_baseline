"""
QUESTION:
Create a function `rearrange_array` that takes an array of integers as input and returns a rearranged array in the order of highest number first, followed by the lowest, then second highest, second lowest, and so on. The function should not use any additional libraries or data structures other than the input array.
"""

def rearrange_array(input_array):
    # sort the array in ascending order
    input_array.sort()
    
    # define an empty result array
    output_array = []

    while input_array:
        # add the largest element
        output_array.append(input_array.pop(-1))
        if input_array:
            # add the smallest element
            output_array.append(input_array.pop(0))
    
    return output_array