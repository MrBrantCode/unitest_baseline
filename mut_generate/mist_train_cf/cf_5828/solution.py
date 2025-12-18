"""
QUESTION:
Write a function `divisible_by_3_and_5` that takes a list of numbers as input. The function should find all the numbers in the list that are divisible by both 3 and 5, calculate the product of their digits, and print the result. The function should use a recursive approach for iteration and should not use any built-in functions or libraries for finding divisors or calculating the product of digits.
"""

def divisible_by_3_and_5(numbers, index=0):
    if index >= len(numbers):
        return
    
    num = numbers[index]
    if num % 3 == 0 and num % 5 == 0:
        digits_product = 1
        for digit in str(num):
            digits_product *= int(digit)
        print(f"Number {num} is divisible by 3 and 5 and the product of its digits is {digits_product}")
        
    divisible_by_3_and_5(numbers, index+1)