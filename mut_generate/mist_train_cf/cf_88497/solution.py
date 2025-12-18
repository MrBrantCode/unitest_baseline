"""
QUESTION:
Create a function named `print_third_highest` that takes a list of integers as input and prints the third highest value from the list, considering duplicates. If the list contains less than three unique elements, the function should print a corresponding message and return without printing any value.
"""

def print_third_highest(lst):
    # Remove duplicates from the list
    unique_lst = list(set(lst))

    # Check if there are at least 3 unique elements
    if len(unique_lst) < 3:
        print("The list doesn't have a third highest value.")
        return

    # Sort the unique list in descending order
    unique_lst.sort(reverse=True)

    # Print the third highest value
    print("The third highest value is:", unique_lst[2])