"""
QUESTION:
Write a function `find_most_common` that takes a list as input and returns the most common element in the list without using any built-in functions or methods that directly solve the problem, such as the `collections` module or the `Counter` class. The function should implement its own logic to solve the problem and handle lists with duplicate elements, returning the element with the highest frequency. If there are multiple elements with the same highest frequency, any of them can be returned.
"""

def entrance(lst):
    # Create an empty dictionary to store the count of each element
    counts = {}

    # Iterate over each element in the list
    for elem in lst:
        # Check if the element is already present in the dictionary
        if elem in counts:
            # If yes, increment its count by 1
            counts[elem] += 1
        else:
            # If not, initialize its count to 1
            counts[elem] = 1

    # Initialize variables to store the most common element and its count
    most_common = None
    max_count = 0

    # Iterate over the counts dictionary
    for elem, count in counts.items():
        # Check if the current element has a higher count than the previous most common element
        if count > max_count:
            # If yes, update the most common element and its count
            most_common = elem
            max_count = count

    # Return the most common element
    return most_common