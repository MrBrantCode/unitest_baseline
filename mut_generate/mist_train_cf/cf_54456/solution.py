"""
QUESTION:
Implement a function called `quick_sort` that takes a list of alphanumeric and special characters as input, removes non-ASCII characters, and returns the sorted list in lexicographical order based on ASCII values. The function should be efficient and able to handle erroneous entries.
"""

def quick_sort(my_list):
    """
    This function sorts the given list in lexicographical order based on ASCII values
    and removes non-ASCII characters.

    Args:
        my_list (list): A list of alphanumeric and special characters.

    Returns:
        list: The sorted list in lexicographical order based on ASCII values.
    """
    # Remove non-ASCII characters from the list
    my_list = [entry for entry in my_list if ord(entry) < 128]

    # Base case: If the list has one or zero elements, it is already sorted.
    if len(my_list) <= 1:
        return my_list
    else:
        # Select the pivot element (in this case, the middle element)
        pivot = my_list[len(my_list) // 2]

        # Divide the list into three sublists: elements less than the pivot, 
        # elements equal to the pivot, and elements greater than the pivot
        left = [x for x in my_list if ord(x) < ord(pivot)]
        middle = [x for x in my_list if ord(x) == ord(pivot)]
        right = [x for x in my_list if ord(x) > ord(pivot)]

        # Recursively sort the sublists and combine the results
        return quick_sort(left) + middle + quick_sort(right)