"""
QUESTION:
Write a function named 'rearrange_and_invert' that takes a list of strings as input. The function should first sort the list in lexicographical order, then reverse the sorted list, and finally return the reversed list along with the original position of each element in the input list.
"""

def rearrange_and_invert(input_list):
    # Create a list of tuples containing each element and its original position
    indexed_list = [(element, index) for index, element in enumerate(input_list)]
    
    # Sort the list of tuples in lexicographical order based on the elements
    sorted_list = sorted(indexed_list, key=lambda x: x[0])
    
    # Reverse the sorted list
    reversed_list = sorted_list[::-1]
    
    # Return the reversed list along with the original position of each element
    return [(element, index) for element, index in reversed_list]