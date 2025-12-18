"""
QUESTION:
Write a function `calculate_result` that takes a list of exactly 7 positive integers as input. The function should perform the following operations: 
1. Subtract the first number from the second number.
2. Multiply the result by the product of the third and fourth numbers.
3. Add the fifth number to the result.
4. Calculate the factorial of the sixth number.
5. Multiply the result by the factorial and then divide by the seventh number.
The function should return the final result as an integer.
"""

def calculate_result(numbers):
    result = numbers[1] - numbers[0]
    result *= numbers[2] * numbers[3]
    result += numbers[4]
    
    factorial = 1
    for i in range(1, numbers[5] + 1):
        factorial *= i
    
    result = (result * factorial) / numbers[6]
    
    return int(result)