"""
QUESTION:
Write a function `find_first_unique_odd_number` that takes a list of positive integers as input and returns the first unique odd number greater than 5 and less than 20. The function should have a time complexity of O(n), where n is the length of the list. If no such number exists, return -1.
"""

def find_first_unique_odd_number(numbers):
    frequency = {}
    
    for num in numbers:
        if num % 2 != 0 and 5 < num < 20:
            if num not in frequency:
                frequency[num] = 1
            else:
                frequency[num] += 1
    
    for num in numbers:
        if num % 2 != 0 and 5 < num < 20 and frequency[num] == 1:
            return num
    
    return -1