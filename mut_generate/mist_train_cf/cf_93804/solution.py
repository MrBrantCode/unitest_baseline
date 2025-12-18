"""
QUESTION:
Create a function `compare_arrays` that compares the elements of multiple input arrays. The function should take a list of arrays as input, where each array contains at most 10 integers ranging from -100 to 100. The function should return or print the elements that are present in all the input arrays, along with the number of arrays each common element appears in.
"""

def compare_arrays(arrays):
    # Create a dictionary to store the count of each element
    count_dict = {}
    # Iterate through each array
    for array in arrays:
        # Iterate through each element in the array
        for element in array:
            # If the element is already in the count_dict, increment the count
            if element in count_dict:
                count_dict[element] += 1
            # Otherwise, initialize the count to 1
            else:
                count_dict[element] = 1
    
    # Create an empty list to store the common elements
    common_elements = []
    # Iterate through each element in the count_dict
    for element, count in count_dict.items():
        # If the count is equal to the number of arrays, it is a common element
        if count == len(arrays):
            common_elements.append((element, count))
    
    # Return the common elements and their counts
    return common_elements