"""
QUESTION:
Function Name: unique_sort
Information: This function determines whether a list of integers can be sorted in ascending order using the following operations: 
- Reversing any sublist indefinitely
- Discarding a single element from the list
- Performing a one-time swap operation on any two elements
Restrictions: The function should return True if the list can be sorted using the above operations and False otherwise. If the list is empty, the function should return True.
"""

def can_be_sorted(numbers: list):
    """
    Returns True if it's possible to sort the numbers list by:
    - reversing any sublist indefinitely, 
    - discarding a single element from the list
    - performing a one-time swap operation on any two elements
    """
    decrease_count = 0
    index = []
    for i in range(len(numbers)-1):
        if numbers[i] > numbers[i+1]:
            decrease_count += 1
            index.append(i)
    if decrease_count == 0:
        return True
    elif decrease_count == 1:
        if (index[0] > 0 and numbers[index[0]-1] <= numbers[index[0]+1]) or\
        (index[0] < len(numbers)-2 and numbers[index[0]] <= numbers[index[0]+2]):
            return True
    elif decrease_count == 2:
        if index[1] == index[0]+1 and\
        ((index[0] >0 and numbers[index[0]-1] <= numbers[index[1]+1]) or\
        (index[1] < len(numbers) - 2 and numbers[index[0]] <= numbers[index[1]+2])):
            return True
    return False