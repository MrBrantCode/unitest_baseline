"""
QUESTION:
Create a function called `insert_and_sort` that takes in a list of integers `test_list`, an integer `inserted_element`, and an integer `index`. The function should insert the `inserted_element` at the specified `index` in `test_list`, sort the list in non-descending order, and return the sorted list. If the `index` is invalid (less than 0 or greater than the length of `test_list`) or if `inserted_element` is not an integer, the function should return an error message.
"""

def insert_and_sort(test_list, inserted_element, index):
    # Check if the inserted element is an integer
    if not isinstance(inserted_element, int):
        return 'Invalid input: Element should be an integer'
    # Check if the index is valid
    if index < 0 or index > len(test_list):
        return 'Invalid index'

    test_list.insert(index, inserted_element)
    test_list.sort()
    return test_list