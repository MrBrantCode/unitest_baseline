"""
QUESTION:
Create a function named 'multiply' that takes a non-empty list of integers as input. The function should return two values: the product of all odd numbers located at even indices in the list and the sum of all even numbers in the list. If there are no odd numbers at even indices, the product should be 1. If there are no even numbers, the sum should be 0.
"""

def entrance(lst):
    # Initialize sum and product variables
    sum_even_nums = 0
    product_odd_nums = 1
    # Iterate over the input list
    for i in range(len(lst)):
        # If index is even and the element is odd, multiply it with the product
        if i % 2 == 0 and lst[i] % 2 != 0:
            product_odd_nums *= lst[i]
        # If the element is even, add it to the sum
        elif lst[i] % 2 == 0:
            sum_even_nums += lst[i]
    # Return the product and sum
    return product_odd_nums, sum_even_nums