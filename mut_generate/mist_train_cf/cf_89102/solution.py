"""
QUESTION:
Implement a function called `multiply_by_two` that takes a list of integers as input, and returns a new list where each number in the input list is multiplied by 2. The function should be implemented using functional programming techniques, have a time complexity of O(n), and a space complexity of O(n), where n is the length of the input list. Do not use any built-in functions or methods that directly solve the problem, such as `map` or list comprehensions. Instead, use basic arithmetic operations, loops, and conditionals to achieve the desired result.
"""

def multiply_by_two(numbers):
    multiplied_numbers = []
    for num in numbers:
        multiplied_numbers.append(num * 2)
    return multiplied_numbers