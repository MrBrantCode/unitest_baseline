"""
QUESTION:
Create a function called `remove_duplicates_and_sort_descending` that takes a list of integers as input, removes all duplicate elements, and returns the result in descending order without using any pre-built sorting functions or other pre-built functions except for the print function.
"""

def remove_duplicates_and_sort_descending(nums):
    """
    This function removes duplicate elements from the input list and returns the result in descending order.

    Args:
        nums (list): A list of integers.

    Returns:
        list: A list of integers with duplicates removed and sorted in descending order.
    """

    # Empty list to store unique elements
    unique_list = []

    # Iterate over the given list
    for num in nums:
        # If the number is not already in unique_list, add it
        if num not in unique_list:
            unique_list.append(num)

    # Now to sort this list in descending order, we can use a simple bubble sort algorithm
    for i in range(len(unique_list)):
        for j in range(len(unique_list)-i-1):  # Last i elements are already in place
            if unique_list[j] < unique_list[j+1]:
                # Swap if the element found is lesser than next element
                unique_list[j], unique_list[j+1] = unique_list[j+1], unique_list[j]

    return unique_list