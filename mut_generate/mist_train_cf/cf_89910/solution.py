"""
QUESTION:
Write a function `max_product(numbers)` that finds the maximum product of four numbers in the list, where the product must include exactly two positive numbers and two negative numbers. The function should have a time complexity of O(n), where n is the length of the list. If the list contains less than four numbers, return "The list must contain at least four numbers." If the list does not contain enough positive and negative numbers, return "The list does not contain enough positive and negative numbers."
"""

def max_product(numbers):
    if len(numbers) < 4:
        return "The list must contain at least four numbers."

    pos_numbers = []
    neg_numbers = []

    for num in numbers:
        if num > 0:
            pos_numbers.append(num)
        elif num < 0:
            neg_numbers.append(num)

    if len(pos_numbers) < 2 or len(neg_numbers) < 2:
        return "The list does not contain enough positive and negative numbers."

    pos_numbers.sort(reverse=True)
    neg_numbers.sort()

    max_product = pos_numbers[0] * pos_numbers[1] * neg_numbers[0] * neg_numbers[1]

    return max_product