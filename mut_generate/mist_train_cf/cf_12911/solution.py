"""
QUESTION:
Create a function `merge_and_sort` that takes two lists as input and returns a new list containing all elements from both lists in descending order. The function should not use built-in list methods such as `append()` or `extend()`, and it should not use the built-in `sorted()` function.
"""

def merge_and_sort(list_1, list_2):
    """
    Merge two lists into one and sort the resulting list in descending order.
    
    Args:
        list_1 (list): The first list to merge.
        list_2 (list): The second list to merge.
    
    Returns:
        list: A new list containing all elements from both lists in descending order.
    """
    new_list = []
    for element in list_1:
        new_list = new_list + [element]
    for element in list_2:
        new_list = new_list + [element]

    # Sorting the new list in descending order
    for i in range(len(new_list)):
        for j in range(i + 1, len(new_list)):
            if new_list[i] < new_list[j]:
                new_list[i], new_list[j] = new_list[j], new_list[i]

    return new_list