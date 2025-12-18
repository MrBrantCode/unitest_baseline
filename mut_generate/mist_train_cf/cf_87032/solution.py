"""
QUESTION:
Write a function called `find_biggest_number` that takes a list of integers `my_list` as a parameter. The function should return the largest number in the list, or None if the list is empty. If the list contains duplicate numbers, any one of the duplicates can be returned. The implementation should have a time complexity of O(n) and not use built-in sorting functions or libraries.
"""

def find_biggest_number(my_list):
    if len(my_list) == 0:
        return None
    
    biggest_number = my_list[0]
    for number in my_list:
        if number > biggest_number:
            biggest_number = number
    
    return biggest_number