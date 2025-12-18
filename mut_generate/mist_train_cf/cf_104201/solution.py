"""
QUESTION:
Create a function named sum_divisible_by_two_and_three that takes a list of integers as an argument. The function should return the total of all elements in the list that are divisible by both 2 and 3. If there are no such elements, return -1.
"""

def sum_divisible_by_two_and_three(lst):
    total = 0
    found = False
    
    for num in lst:
        if num % 2 == 0 and num % 3 == 0:
            total += num
            found = True
    
    if found:
        return total
    else:
        return -1