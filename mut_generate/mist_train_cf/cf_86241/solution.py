"""
QUESTION:
Design a function named `count_duplicates` to delete duplicates from a list, while keeping track of the count of each duplicate element. The function should maintain the order of the original list and return a new list with the unique elements along with their respective counts as tuples. The function must be implemented without using any built-in Python functions or libraries and should have a time complexity of O(n), where n is the length of the input list. The input list can contain duplicate elements and negative numbers.
"""

def count_duplicates(lst):
    # Create an empty dictionary to store the count of each element
    count_dict = {}
    # Create an empty list to store the unique elements with their counts
    unique_list = []

    # Iterate through the input list
    for num in lst:
        # Check if the element is already in the dictionary
        if num in count_dict:
            # If it is, increment its count by 1
            count_dict[num] += 1
        else:
            # If it is not, add it to the dictionary with a count of 1
            count_dict[num] = 1

    # Iterate through the input list again
    for num in lst:
        # Check if the count of the element is greater than 0
        if count_dict[num] > 0:
            # If it is, add the element and its count as a tuple to the unique list
            unique_list.append((num, count_dict[num]))
            # Set the count of the element to 0 to mark it as visited
            count_dict[num] = 0

    # Return the unique list
    return unique_list