"""
QUESTION:
Write a function named `get_even_and_sort` that takes a list of integers as input and returns a new list containing only the even integers from the input list, sorted in descending order. The function must not use built-in sort functions like `sort()` or `sorted()`. Instead, it should implement a custom sorting algorithm within a nested `swap_elements` function.
"""

def get_even_and_sort(numbers: list):
    """Returns a new list containing only the even integers from the input list, sorted in descending order."""
    
    def swap_elements(num_list, index1, index2):
        """Swaps two elements in a list by index."""
        temp = num_list[index1]
        num_list[index1] = num_list[index2]
        num_list[index2] = temp

    even_numbers = [num for num in numbers if num % 2 == 0]
    
    # Implement bubble sort to sort the even numbers in descending order
    for i in range(len(even_numbers)):
        for j in range(len(even_numbers) - 1):
            if even_numbers[j] < even_numbers[j + 1]:
                swap_elements(even_numbers, j, j + 1)

    return even_numbers