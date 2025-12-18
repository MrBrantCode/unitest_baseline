"""
QUESTION:
Implement a function `binary_search_animal` that searches for a specific animal in a given list of animals in alphabetical order using a binary search algorithm. The function should take two parameters: `animal_list` and `target_animal`. If the `target_animal` is found in the list, the function should return its index; otherwise, it should return -1.
"""

def binary_search_animal(animal_list, target_animal):
    left = 0
    right = len(animal_list) - 1

    while left <= right:
        mid = (left + right) // 2
        if animal_list[mid] == target_animal:
            return mid
        elif animal_list[mid] < target_animal:
            left = mid + 1
        else:
            right = mid - 1

    return -1