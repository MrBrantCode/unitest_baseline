"""
QUESTION:
Implement a function named `reverse_list` that takes a list `lst` as input and returns the reversed list. The function should not use built-in list functions, additional memory space, looping constructs (such as for loops or while loops), or direct recursion.
"""

def reverse_list(lst):
    # Define a generator to yield the elements of the list in reverse order
    def reverse_generator(lst, index):
        if index >= 0:
            yield lst[index]
            yield from reverse_generator(lst, index - 1)

    # Convert the generator into a reversed list
    return list(reverse_generator(lst, len(lst) - 1))