"""
QUESTION:
Write a function called "separate_elements" that takes an array as input. Loop through each element in the array, check if the element is an integer and divisible by 3, not divisible by 3, or a string. Store the integers divisible by 3 in a list, integers not divisible by 3 in another list, and append " Not a number" to each string before storing in a third list.
"""

def separate_elements(data):
    numbers_divisible_by_3 = []
    numbers_not_divisible_by_3 = []
    non_numbers = []

    for element in data:
        if isinstance(element, int) and element % 3 == 0:
            numbers_divisible_by_3.append(element)
        elif isinstance(element, int) and element % 3 != 0:
            numbers_not_divisible_by_3.append(element)
        elif isinstance(element, str):
            non_numbers.append(element + " Not a number")
            
    return numbers_divisible_by_3, numbers_not_divisible_by_3, non_numbers