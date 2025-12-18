"""
QUESTION:
Create a function named `sum_even` that calculates the sum of even numbers in a given list. The function should only return the sum if the list contains more than three even numbers and the sum of odd numbers in the list is greater than or equal to 100. Use the modulus operator (`%`) to determine if a number is even or odd.
"""

def sum_even(lst):
    even_nums = [num for num in lst if num % 2 == 0]
    odd_nums = [num for num in lst if num % 2 != 0]
    if len(even_nums) > 3 and sum(odd_nums) >= 100:
        return sum(even_nums)
    else:
        return None