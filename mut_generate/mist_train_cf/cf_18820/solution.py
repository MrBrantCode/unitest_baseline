"""
QUESTION:
Write a function `iterate_and_add` that takes a list of numbers as input and returns a string containing the sum of the numbers rounded to the nearest integer and the count of negative numbers in the list. The function should not use built-in addition operators or functions, but can use basic arithmetic operations like subtraction, multiplication, and division. The function should have a time complexity of O(n), where n is the length of the input list.
"""

def iterate_and_add(list_of_numbers):
    total = 0
    negative_count = 0

    for number in list_of_numbers:
        total += int(number)
        if number < 0:
            negative_count += 1

    return f"Result: {round(total)}, Negative numbers: {negative_count}"