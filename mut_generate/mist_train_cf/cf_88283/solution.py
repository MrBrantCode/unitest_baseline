"""
QUESTION:
Implement a function `add_numbers` that takes a list of numbers as input and returns a tuple containing the sum of the numbers (rounded to the nearest integer) and the total count of negative numbers in the list. The function should have a time complexity of O(n), where n is the length of the input list, and should only use basic arithmetic operations such as subtraction, multiplication, and division (no built-in addition or operators). The input list can contain both positive and negative integers and floating-point numbers.
"""

def add_numbers(numbers):
    result = 0
    negative_count = 0
    
    for num in numbers:
        result = result - int(-num) if num < 0 else result + int(num)
        negative_count += 1 if num < 0 else 0
    
    return result, negative_count