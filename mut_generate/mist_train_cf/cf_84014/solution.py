"""
QUESTION:
Write a function `sum_of_numbers` that takes in a list of numbers as input and returns two values: the sum of all the numbers in the list and the count of numbers greater than 10. The function should be able to handle lists containing various data types, including strings, special characters, and empty lists, by ignoring non-numeric values. The function should not throw any errors for such inputs.
"""

def sum_of_numbers(num_list):
    sum = 0
    count = 0
    for num in num_list:
        if isinstance(num, int) or isinstance(num, float):
            sum += num
            if num > 10:
                count += 1
    return sum, count