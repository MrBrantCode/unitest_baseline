"""
QUESTION:
Create a function named `delete_last_occurrence(input_list, value)` that deletes the last occurrence of a specified value from a list without using any built-in functions or methods. The function should return a new list, leaving the original list unmodified. The function must run in O(n) time complexity and O(1) space complexity, where n is the number of elements in the list, and it cannot use additional data structures or sort of string manipulation or conversion functions.
"""

def delete_last_occurrence(input_list, value):
    index = None
    for i in range(len(input_list)-1, -1, -1):
        if input_list[i] == value:
            index = i
            break
    if index is None:
        return input_list
    new_list = input_list[:]
    del new_list[index]
    return new_list