"""
QUESTION:
Create a function `custom_sort(numbers)` that determines if a list of integers can be sorted in non-decreasing order by performing the following operations:
- Reverse any sublist any number of times
- Remove one element from the list
- Swap two elements once
Return True if the list can be sorted, False otherwise. If the input list is empty, return True.
"""

def custom_sort(numbers):
    """
    We have a list 'numbers' of N integers numbers[1], numbers[2], ..., numbers[N]. The
    numbers in the list will be randomly ordered. Your task is to determine if
    it is possible to get a list sorted in non-decreasing order by performing
    the following operations on the given list:
        1. You can perform reverse operation on any sublist any number of times.
        2. You are allowed to remove one element from the list.
        3. You can perform a swap operation on any two elements once.
        
    Using the given operations, determine if it is possible to obtain a sorted list.
    If it is possible, return True, else return False.
    If the given list is empty, return True.

    Note: The given list may or may not have unique elements.
    """
    if len(numbers) == 0:
        return True
    
    inversions = 0
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] > numbers[j]:
                inversions += 1
    
    if inversions % 2 == 0:
        return True
    
    for i in range(len(numbers)):
        temp = numbers[:i] + numbers[i+1:]
        inversions = 0
        for j in range(len(temp)):
            for k in range(j+1, len(temp)):
                if temp[j] > temp[k]:
                    inversions += 1

        if inversions % 2 == 0:
            return True
    
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            temp = numbers[:i] + [numbers[j]] + numbers[i+1:j] + [numbers[i]] + numbers[j+1:]
            inversions = 0
            for k in range(len(temp)):
                for l in range(k+1, len(temp)):
                    if temp[k] > temp[l]:
                        inversions += 1

            if inversions % 2 == 0:
                return True
    
    return False