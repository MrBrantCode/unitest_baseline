"""
QUESTION:
Create a function called `bubble_sort` that takes a list of integers as input and returns a new list containing the same integers in ascending order. The function should not use any built-in sorting functions, and it should sort the list in-place by repeatedly iterating over the list and swapping adjacent elements if they are in the wrong order.
"""

def entance(number_list: list) -> list:
    list_length = len(number_list)
    for i in range(list_length-1):
        # Last i elements are already in place
        for j in range(0, list_length-i-1):
            # traverse the list from 0 to length-i-1
            # Swap if the element found is greater than the next element
            if number_list[j] > number_list[j+1] :
                number_list[j], number_list[j+1] = number_list[j+1], number_list[j]
    return number_list