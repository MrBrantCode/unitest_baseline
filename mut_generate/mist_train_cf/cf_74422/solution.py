"""
QUESTION:
Create a function `process_list` that takes a 2D list of integers as input and returns a list of sums. For each subarray in the input list, create a new list containing only the first and last elements, then calculate the sum of this new list. If a subarray contains non-integer values, skip it. The function should return a list where each element at index `i` is the sum of the new list generated from the subarray at index `i` in the input list.
"""

def process_list(my_list):
    # Initialize the sums to 0.
    sums = [0] * len(my_list)

    for i in range(len(my_list)):
        sublist = my_list[i]
        # Check if the current subarray has non-integer types, if so skip to next iteration
        if not all(isinstance(item, int) for item in sublist):
            continue
        # Create a new list based on the first and last elements.
        new_list = [sublist[0], sublist[-1]]
        # Add the new list's sum to the corresponding position in 'sums'.
        sums[i] += sum(new_list)

    return sums