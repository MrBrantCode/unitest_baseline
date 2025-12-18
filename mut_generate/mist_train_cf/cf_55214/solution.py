"""
QUESTION:
Construct a Python function named `mean_of_trio` that calculates the mean of the three smallest and three largest integers in a given list. The input is a list of integers and the output should be two floats representing the mean of the smallest trio and the mean of the largest trio.
"""

def mean_of_trio(lst):
    # sort list in ascending order
    sorted_list_asc = sorted(lst)
    
    # sort list in descending order
    sorted_list_desc = sorted(lst, reverse=True)

    # select the first three elements
    smallest_trio = sorted_list_asc[:3]
    largest_trio = sorted_list_desc[:3]

    # calculate the mean 
    mean_smallest_trio = sum(smallest_trio) / len(smallest_trio)
    mean_largest_trio = sum(largest_trio) / len(largest_trio)

    return mean_smallest_trio, mean_largest_trio