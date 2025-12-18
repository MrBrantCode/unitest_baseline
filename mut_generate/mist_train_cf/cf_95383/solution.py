"""
QUESTION:
Implement a function `iterate_and_add` that takes a list of numbers as input, where the numbers can be either integers or floating-point numbers. The function should iterate over the list and calculate the sum of the numbers without using the built-in addition operator or function. Instead, it should use basic arithmetic operations like subtraction, multiplication, and division. The result of the addition should be rounded to the nearest integer. Additionally, the function should count the total number of negative numbers in the list and return the count along with the final result. The function should have a time complexity of O(n), where n is the length of the input list.
"""

def iterate_and_add(list_of_numbers):
    total = 0
    negative_count = 0

    for number in list_of_numbers:
        total += int(number)
        if number < 0:
            negative_count += 1

    return round(total), negative_count