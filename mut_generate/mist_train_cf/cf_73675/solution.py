"""
QUESTION:
Given a function `advam` that takes a list of numbers as input, return a tuple containing a boolean value indicating whether the list can be sorted by at most one operation (either removing one element or swapping two adjacent elements) and a list of actions taken to sort the list. If the list is already sorted or can be sorted by one operation, return `True` along with the actions. Otherwise, return `False` along with an empty list.
"""

def advam(numbers):
    actions = []

    if not numbers:
        return True, actions

    numbers_with_indexes = list(enumerate(numbers))
    numbers_with_indexes.sort(key = lambda x: x[1])

    place_of_violation = -1
    for i in range(len(numbers) - 1):
        if numbers_with_indexes[i][0] > numbers_with_indexes[i + 1][0]:
            place_of_violation = i
            break

    if place_of_violation == -1:
        return True, actions

    removed = numbers_with_indexes.pop(place_of_violation)
    actions.append(f"Removed {removed[1]}")

    is_sorted = True
    for i in range(len(numbers_with_indexes) - 1):
        if numbers_with_indexes[i][0] > numbers_with_indexes[i + 1][0]:
            is_sorted = False
            break

    if is_sorted:
        return True, actions

    numbers_with_indexes.insert(place_of_violation, removed)
    actions.pop()

    numbers_with_indexes[place_of_violation], numbers_with_indexes[place_of_violation + 1] = \
    numbers_with_indexes[place_of_violation + 1], numbers_with_indexes[place_of_violation]        
    actions.append(f"Swapped {numbers_with_indexes[place_of_violation][1]} with \
    {numbers_with_indexes[place_of_violation + 1][1]}")

    is_sorted = True
    for i in range(len(numbers_with_indexes) - 1):
        if numbers_with_indexes[i][0] < numbers_with_indexes[i + 1][0]:
            is_sorted = False
            break

    if is_sorted:
        return True, actions

    return False, []