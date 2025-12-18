"""
QUESTION:
Write a function called `find_odd_number` that takes a list of integers as input. The function should return the first number in the list that appears an odd number of times. If no such number exists, the function should return -1.
"""

def find_odd_number(arr):
    count_dict = {}
    
    for num in arr:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    for num, count in count_dict.items():
        if count % 2 != 0:
            return num
    
    return -1