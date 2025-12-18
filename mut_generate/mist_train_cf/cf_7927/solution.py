"""
QUESTION:
Create a function named `calculate_result` that takes a list of exactly 7 positive integers as input. The function should perform the following operations:
- Subtract the first number from the second number and store the result.
- Multiply the third number by the fourth number and add the result to the stored result.
- Add the fifth number to the result from the previous step.
- Calculate the factorial of the sixth number.
- Multiply the stored result by the factorial and then divide by the seventh number.

Return the final result as an integer.
"""

def calculate_result(numbers):
    result = numbers[1] - numbers[0]
    result += numbers[3] * numbers[2]
    result += numbers[4]
    
    factorial = 1
    for i in range(1, numbers[5] + 1):
        factorial *= i
    
    result = (result * factorial) / numbers[6]
    
    return int(result)