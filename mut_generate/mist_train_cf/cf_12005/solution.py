"""
QUESTION:
Implement a function `most_frequent_element` that takes a list of integers as input and returns the element that appears most frequently, considering only elements that appear at least twice. The input list will contain at most 10^6 elements, and each element will be an integer between 0 and 10^9. If no such element exists, return None.
"""

def most_frequent_element(lst):
    # Create a dictionary to keep track of element counts
    count_dict = {}

    # Iterate through the list and update the counts
    for element in lst:
        if element in count_dict:
            count_dict[element] += 1
        else:
            count_dict[element] = 1

    # Find the element with the maximum count that appears at least twice
    max_count = 0
    max_element = None
    for element, count in count_dict.items():
        if count >= 2 and count > max_count:
            max_count = count
            max_element = element

    return max_element