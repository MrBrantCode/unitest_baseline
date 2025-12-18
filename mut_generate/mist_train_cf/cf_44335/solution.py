"""
QUESTION:
Create a function called custom_sort that takes a list of integers as input. The function should determine if it's possible to get a sorted list in non-decreasing order by either removing one element or reversing any sublist any number of times. The function should return True if it's possible to obtain a sorted list, otherwise return False. If the input list is empty, the function should return True.
"""

def custom_sort(numbers):
    if len(numbers) == 0:
        return True
    for i in range(len(numbers)):
        new_list = numbers[:i] + numbers[i+1:]
        sorted_list = sorted(new_list)
        if new_list == sorted_list:
            return True
        if numbers[i:] == sorted(numbers[i:])[::-1]:
            return True
    return False