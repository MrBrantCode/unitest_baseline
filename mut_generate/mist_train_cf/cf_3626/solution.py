"""
QUESTION:
Create a function called `find_second_highest` that takes a list of integers as input and returns the second highest unique number in the list. If the list has less than two elements, return None. If the second highest number is not unique, return the next unique highest number, and so on. The list can contain both positive and negative integers.
"""

def find_second_highest(numbers):
    if len(numbers) < 2:
        return None

    unique_numbers = sorted(set(numbers), reverse=True)
    second_highest = unique_numbers[1] if len(unique_numbers) >= 2 else unique_numbers[0]

    if numbers.count(second_highest) > 1:
        return find_second_highest([num for num in numbers if num != second_highest])
    else:
        return second_highest