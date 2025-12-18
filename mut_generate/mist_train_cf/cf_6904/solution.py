"""
QUESTION:
Create a function `create_new_array` that takes two parameters: `input_list` and `size`. The function should return a new list of a given size by copying unique elements from the input list. The function should handle arrays of any data type and have a time complexity of O(n), where n is the length of the input array. The function should also be able to efficiently handle arrays with duplicate elements, removing duplicates with a time complexity of O(n) or less.
"""

def create_new_array(input_list, size):
    # Remove duplicates from the original array
    unique_list = list(set(input_list))
    
    # Create the new array with unique elements
    new_array = []
    for i in unique_list:
        new_array.append(i)
        if len(new_array) == size:
            break
    
    return new_array