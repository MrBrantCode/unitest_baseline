"""
QUESTION:
Create a function `multiply_abs_values_v2` that takes a list of numbers as input. The function should return the product of the absolute values of these numbers, rounded down to the nearest integer, excluding any numbers that are divisible by 2, 3, or 5. If the list contains a zero, the function should return 0.
"""

def multiply_abs_values_v2(lst):
    def is_excluded(num):
        """
        Check if the number is divisible by any prime number less than or equal to 5.
        """
        for i in [2, 3, 5]:
            if num % i == 0:
                return True
        return False

    product = 1
    for num in lst:
        num = int(abs(num))
        if not is_excluded(num) and num != 0:
            product *= num
    
    return product