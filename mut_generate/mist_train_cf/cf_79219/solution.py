"""
QUESTION:
Write a function `count_elements_in_3d_array` that takes a 3D array as input and returns a tuple containing two values: the total count of unique elements in the whole 3D array, and a dictionary where the keys are the indices of the 2D arrays and the values are the counts of repeating elements in the respective 2D arrays. The 3D array is a list of lists of lists of integers.
"""

def count_elements_in_3d_array(array):
    # A set to hold unique elements and a dictionary to hold repeating elements count
    unique_elements = set()
    repeating_elements_in_2d_arrays = {}

    # Iterate through the 3D array
    for i, two_d_array in enumerate(array):
        # A set to hold elements in the current 2D array
        elements_in_2d_array = set()
        # A count to keep track of repeating elements in the current 2D array
        repeating_elements_count = 0

        # Iterate through each 2D array
        for one_d_array in two_d_array:
            for element in one_d_array:
                # If the element is already in the 2D array set, increment the repeating count
                if element in elements_in_2d_array:
                    repeating_elements_count += 1
                else:
                    elements_in_2d_array.add(element)
                unique_elements.add(element)

        # Add the repeating count to the dictionary
        repeating_elements_in_2d_arrays[i] = repeating_elements_count

    # Return the count of unique elements and the repeating elements count
    return len(unique_elements), repeating_elements_in_2d_arrays