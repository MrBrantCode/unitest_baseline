"""
QUESTION:
Create a function named `check_list` that takes in a list of integers. The function should check if all elements in the list are unique, are in ascending order, and are even numbers. The function should return a tuple containing the total count of unique elements, the sum of all elements in the list, and a new list where each element is multiplied by its index position. The input list must only contain even integers, be in ascending order, and have no duplicates; otherwise, return "Invalid input".
"""

def check_list(lst):
    if not lst:  
        return (0, 0, [])

    unique_elements = set()
    total_sum = 0
    new_list = []

    for i, num in enumerate(lst):
        if not isinstance(num, int):  
            return "Invalid input"

        if num % 2 != 0:  
            return "Invalid input"

        if num in unique_elements:  
            return "Invalid input"

        if lst.index(num) != i:
            return "Invalid input"

        unique_elements.add(num)
        total_sum += num
        new_list.append(i * num)

    return (len(unique_elements), total_sum, new_list)