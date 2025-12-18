"""
QUESTION:
Create a function named `process_array` that takes a list of integers as input. The function should duplicate the input list, subtract 7 from each element in the new list, and then sort the new list in descending order. If the input list is empty, the function should return an error message.
"""

def process_array(your_list):
    # Check if the list is empty
    if not your_list:
        return "Error: The array is empty"
    else:
        # Duplicate the array and subtract 7 from each element
        new_list = [item - 7 for item in your_list * 2]

        # Sort the array in descending order
        new_list.sort(reverse=True)

    return new_list