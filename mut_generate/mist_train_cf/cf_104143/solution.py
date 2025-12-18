"""
QUESTION:
Create a function called `add_lists` that takes two lists of integers as input. The function should return a new list containing the sum of corresponding values from the input lists. However, if both corresponding values are divisible by 3, the function should return their product instead of the sum. The input lists must be of equal length and contain at least 3 elements. If the input lists do not meet these length requirements, the function should return an error message.
"""

def add_lists(list1, list2):
    if len(list1) != len(list2) or len(list1) < 3 or len(list2) < 3:
        return "Error: The length of both lists should be equal and greater than 2."

    new_list = []
    for i in range(len(list1)):
        if list1[i] % 3 == 0 and list2[i] % 3 == 0:
            new_list.append(list1[i] * list2[i])
        else:
            new_list.append(list1[i] + list2[i])
    
    return new_list