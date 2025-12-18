"""
QUESTION:
Create a function called `rearrange_to_desc` that takes a multi-dimensional array as input, where the array contains four inner arrays, each with three integer elements in ascending order. The function should rearrange all numbers in the multi-dimensional array to descending order and return the result as a new multi-dimensional array, still containing four inner arrays with three elements each.
"""

def rearrange_to_desc(multi_array):
    # Flatten the multi dimensional array
    flat_array = [num for sublist in multi_array for num in sublist]
    # Sort the flat array in descending order
    desc_sorted_array = sorted(flat_array, reverse=True)
    # Convert the flat array back to multi dimensional array
    desc_multi_array = [desc_sorted_array[i:i+3] for i in range(0, len(desc_sorted_array), 3)]
    return desc_multi_array