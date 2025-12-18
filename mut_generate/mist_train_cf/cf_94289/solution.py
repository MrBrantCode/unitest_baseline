"""
QUESTION:
Implement a function `find_single(arr)` that finds the index of the element that occurs only once in the given array without using any built-in functions or libraries. The function should return the index of the single element if found, otherwise return -1.
"""

def find_single(arr):
    # Create an empty dictionary to store the count of each element
    count_dict = {}
    
    # Iterate over each element in the array
    for element in arr:
        # If the element is already in the dictionary, increment its count
        if element in count_dict:
            count_dict[element] += 1
        # Otherwise, add the element to the dictionary with a count of 1
        else:
            count_dict[element] = 1
    
    # Iterate over the dictionary and find the element with a count of 1
    for element, count in count_dict.items():
        if count == 1:
            # Return the index of the first occurrence of the element in the array
            return arr.index(element)
    
    # If no element with a count of 1 is found, return -1
    return -1