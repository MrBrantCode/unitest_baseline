"""
QUESTION:
Create a function named `check_list` that takes a list of integers as input. The function should check if all elements in the list are unique, in ascending order, and even numbers. The function should return a tuple containing the total count of unique elements, the sum of all elements in the list, and a new list where each element is multiplied by its index position. The input list may be empty or contain non-integer values. The time complexity of the function should be less than O(n^2).
"""

def check_list(lst):
    if not lst:  # check if the list is empty
        return (0, 0, [])

    unique_elements = set()
    total_sum = 0
    new_list = []

    for i, num in enumerate(lst):
        if not isinstance(num, int):  # check if the element is not an integer
            return "Invalid input"

        if num % 2 != 0:  # check if the element is not even
            return "Invalid input"

        if num in unique_elements:  # check if the element is not unique
            return "Invalid input"

        unique_elements.add(num)
        total_sum += num
        new_list.append(i * num)

    return (len(unique_elements), total_sum, new_list)