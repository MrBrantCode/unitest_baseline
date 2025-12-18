"""
QUESTION:
Combine two lists into a new list without duplicates and in alphabetical order. Do not use any built-in sorting or deduplication functions/methods. Implement a function named `combine_lists` that takes two lists as arguments and returns the combined list.
"""

def combine_lists(list_one, list_two):
    # Create a new list to store the combined values
    combined_list = []

    # Iterate over each element in list_one
    for element in list_one:
        # Check if the element is not already in the combined_list
        if element not in combined_list:
            # Append the element to the combined_list
            combined_list.append(element)

    # Iterate over each element in list_two
    for element in list_two:
        # Check if the element is not already in the combined_list
        if element not in combined_list:
            # Append the element to the combined_list
            combined_list.append(element)

    # Sort the combined_list alphabetically
    sorted_combined_list = []

    # Iterate over each element in the combined_list
    for element in combined_list:
        # Find the correct position to insert the element in the sorted_combined_list
        index = 0
        while index < len(sorted_combined_list) and element > sorted_combined_list[index]:
            index += 1
        # Insert the element at the correct position
        sorted_combined_list.insert(index, element)

    # Return the sorted combined list
    return sorted_combined_list