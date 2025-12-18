"""
QUESTION:
Write a function named `advanced_sort` that takes a list of integers `numbers` as input and returns a boolean value indicating whether the list can be sorted in non-descending order by performing the following operations: 
- Inverting any sublist any number of times.
- Removing a single element from the list.
- Swapping any two elements only once.
 
The function should also return the sequence of actions performed to sort the list, if possible. If the list is empty, return True.
"""

def advanced_sort(numbers):
    actions = []
    
    if not numbers:
        return True, actions

    numbers_with_indexes = list(enumerate(numbers))
    numbers_with_indexes.sort(key = lambda x:x[1])
    
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
        if numbers_with_indexes[i][0] > numbers_with_indexes[i + 1][0]:
            is_sorted = False
            break
    
    if is_sorted:
        return True, actions
        
    return False, []