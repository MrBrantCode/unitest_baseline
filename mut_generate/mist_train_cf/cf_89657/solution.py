"""
QUESTION:
Create a function called `create_new_array` that takes an input list of any data type and an integer size as parameters. The function should create a new list by copying unique elements from the input list, removing any duplicates in the process, and truncating the new list to the specified size. The function should have a time complexity of O(n), where n is the length of the input list.
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