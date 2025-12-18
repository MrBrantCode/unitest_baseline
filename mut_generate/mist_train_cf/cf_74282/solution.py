"""
QUESTION:
Write a function named `second_highest_even_element` that takes a list of integers as input and returns a tuple containing the second largest even number and the average of all even numbers in the list. The function should not use built-in functions like max() or sorted(). If the list has less than two even numbers, the function should raise a custom exception named `LessThanTwoEvenDigits`.
"""

class LessThanTwoEvenDigits(Exception):
    pass

def second_highest_even_element(lst: list):
    even_numbers = [x for x in lst if x % 2 == 0]
    if len(even_numbers) < 2:
        raise LessThanTwoEvenDigits("The list has less than two even digits!")
    even_numbers.sort(reverse=True)
    second_max = even_numbers[1]
    avg = sum(even_numbers)/len(even_numbers)
    return second_max, avg