"""
QUESTION:
Write a function `find_median(num_list)` that takes a list of numbers as input and returns the median. The function should be able to handle both sorted and unsorted lists, as well as lists with duplicate entries and lists of odd or even length. The function should have the best possible time complexity for sorting and determining the median.
"""

def find_median(num_list):
    num_list.sort()  # Sort the list in ascending order
    n = len(num_list)
    if n % 2 == 0:  # Check if the list length is even
        median = (num_list[n//2 - 1] + num_list[n//2]) / 2  # Average the two middle values
    else:
        median = num_list[n//2]  # Middle value
    return median