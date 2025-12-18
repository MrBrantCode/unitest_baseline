"""
QUESTION:
Write a function called `find_min_max` that takes a list of integers as input and returns the smallest and largest numbers from the list, without using any built-in functions or libraries for finding the minimum and maximum values.
"""

def find_min_max(numbers):
    # Initialize min_num and max_num as the first number in the list
    min_num = numbers[0]
    max_num = numbers[0]

    # Iterate through the list and update min_num and max_num if a smaller or larger number is found
    for num in numbers:
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num

    return min_num, max_num