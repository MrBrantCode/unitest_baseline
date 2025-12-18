"""
QUESTION:
Create a function `sum_of_third_elements` that takes a list of integers as input. The function should return a new list containing the sum of every 4th element starting from the second element (index 1), every 4th element being the second, sixth, tenth, fourteenth and so on, and each sum should be of every third element starting from the second element. The function should implement a loop that traverses the given list and keep track of the index position.
"""

def sum_of_third_elements(lst):
    new_lst = []
    counter = 1
    running_sum = 0
    for i in range(1, len(lst)):
        if (i-1) % 4 == 0 and (i+1) % 3 == 0:
            running_sum += lst[i]
        if (i+1) % 12 == 0:
            new_lst.append(running_sum)
            running_sum = 0
    return new_lst