"""
QUESTION:
Write a function called `find_biggest_number` that takes a list of integers `my_list` as a parameter. The function should return the largest integer in the list, or `None` if the list is empty. The function should have a time complexity of O(n), where n is the length of the list.
"""

def find_biggest_number(my_list):
    if len(my_list) == 0:
        return None
    
    biggest_number = my_list[0]
    for number in my_list:
        if number > biggest_number:
            biggest_number = number
    
    return biggest_number