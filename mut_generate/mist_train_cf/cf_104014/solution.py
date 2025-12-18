"""
QUESTION:
Write a function `reverse_even_numbers` that takes a list of integers as input, reverses the order of the even numbers, and returns a new list containing only the even numbers in reversed order. The original list and the order of odd numbers should not be altered in the new list.
"""

def reverse_even_numbers(lst):
    even_numbers = [num for num in lst if num % 2 == 0]
    even_numbers.reverse()
    new_list = []
    even_index = 0
    
    for num in lst:
        if num % 2 == 0:
            new_list.append(even_numbers[even_index])
            even_index += 1
        else:
            new_list.append(num)
    
    return [num for num in new_list if num % 2 == 0]