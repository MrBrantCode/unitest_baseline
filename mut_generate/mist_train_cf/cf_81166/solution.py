"""
QUESTION:
Implement a function `filter_negative_and_sort` that takes a list of integers as input and returns a new list containing only the unique negative integers from the input list, sorted in descending order. Write an auxiliary function `rearrange_elements` to sort the list without using the built-in `sort()` or `sorted()` functions in Python.
"""

def filter_negative_and_sort(numbers: list) -> list:
    """
    Returns a new list containing only the unique negative integers from the input list, sorted in descending order.

    :param numbers: A list of integers
    :return: A list of unique negative integers in descending order
    """

    def rearrange_elements(n: list) -> list:
        # Auxiliary function to sort the list without using built-in sort() or sorted() functions
        for i in range(len(n)):
            for j in range(i + 1, len(n)):
                if n[i] < n[j]:
                    n[i], n[j] = n[j], n[i]
        return n

    # Filter unique negative numbers
    filtered_numbers = [num for num in set(numbers) if num < 0]
    
    # Sort the filtered numbers in descending order
    return rearrange_elements(filtered_numbers)