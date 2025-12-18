"""
QUESTION:
Write a function named `calculate_sum` that takes a list of numbers as input and calculates the sum of all elements in the list. The function should return the sum multiplied by 2 if it is divisible by 2 and greater than 10. If the sum is divisible by 2 but less than or equal to 10, return the sum multiplied by 3. If the sum is not divisible by 2 but greater than 10, return the sum divided by 2 and rounded to the nearest integer. If the sum is not divisible by 2 and less than or equal to 10, return the sum divided by 3 and rounded to the nearest integer.
"""

def calculate_sum(my_list):
    total = sum(my_list)
    
    if total % 2 == 0:
        if total > 10:
            return total * 2
        else:
            return total * 3
    else:
        if total > 10:
            return round(total / 2)
        else:
            return round(total / 3)