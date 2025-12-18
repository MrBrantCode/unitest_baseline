"""
QUESTION:
Write a function called `merge_and_sort_lists` that takes two lists as input and returns a new list with the elements from the first list followed by the elements from the second list. The function should remove any duplicate elements from the new list and sort it in descending order without using any built-in list methods or functions such as `append()`, `extend()`, or `sort()`.
"""

def merge_and_sort_lists(list_1, list_2):
    # Combine the two lists
    new_list = []
    for element in list_1:
        new_list += [element]
    for element in list_2:
        new_list += [element]

    # Remove duplicate elements
    unique_list = []
    for element in new_list:
        if element not in unique_list:
            unique_list += [element]
    new_list = unique_list

    # Sort the new list in descending order
    for i in range(len(new_list)):
        max_idx = i
        for j in range(i+1, len(new_list)):
            if new_list[j] > new_list[max_idx]:
                max_idx = j
        new_list[i], new_list[max_idx] = new_list[max_idx], new_list[i]

    return new_list