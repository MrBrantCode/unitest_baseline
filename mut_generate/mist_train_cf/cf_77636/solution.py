"""
QUESTION:
Create a function named `compute_range` that takes two parameters: `start` and `end`, which represent a range of positive natural numbers. This function should calculate the cumulative sum and cumulative product of the individual digits of all numbers within this range. The function should handle potential zeros in the multiplication sequence by avoiding multiplication by zero. Return the total cumulative sum and total cumulative product for all the numbers in the range.
"""

def compute_range(start, end):
    # Initialize total sum and product as 0 and 1 respectively
    total_sum = 0
    total_product = 1
    for num in range(start, end+1):
        digits_sum = 0
        digits_product = 1
        for digit in str(num): 
            digits_sum += int(digit)
            if int(digit) != 0:
                digits_product *= int(digit)
        total_sum += digits_sum
        if digits_product != 1:
            total_product *= digits_product
    return total_sum, total_product