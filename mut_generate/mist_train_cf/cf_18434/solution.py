"""
QUESTION:
Create a function `sort_even_numbers` that takes a list of integers as input. The function should return a new list containing only the even numbers from the original list, sorted in ascending order. The function must not use any built-in sorting functions or libraries.
"""

def entrance(lst):
    even_numbers = [num for num in lst if num % 2 == 0]
    for i in range(len(even_numbers)):
        for j in range(i+1, len(even_numbers)):
            if even_numbers[i] > even_numbers[j]:
                even_numbers[i], even_numbers[j] = even_numbers[j], even_numbers[i]
    return even_numbers