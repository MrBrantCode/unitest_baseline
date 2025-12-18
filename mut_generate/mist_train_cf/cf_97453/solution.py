"""
QUESTION:
Write a function `calculate_sum` that takes a list of integers as input and returns the sum of its unique elements. The function should not use any built-in functions or libraries that directly calculate the sum of a list. It should account for edge cases such as an empty list, a list with only one element, and a list with all negative elements.
"""

def calculate_sum(my_list):
    # Create an empty set to store unique elements
    unique_elements = set()
    
    # Iterate through each element in the list
    for element in my_list:
        # Add the element to the set
        unique_elements.add(element)
    
    # Initialize the sum to 0
    sum_of_elements = 0
    
    # Iterate through each unique element in the set
    for unique_element in unique_elements:
        # Add the unique element to the sum
        sum_of_elements += unique_element
    
    # Return the sum
    return sum_of_elements