"""
QUESTION:
Implement a function named `median` that takes a list of numbers as input and returns the median. The list can contain a mix of integers, floats, and complex numbers. The function should only consider the real part of complex numbers and ignore non-numeric data types. The function must handle invalid inputs by raising exceptions and should not use built-in functions to compute the median. Note that achieving constant time complexity is not feasible for this problem.
"""

def median(numbers):
    try:
        # Get only real parts of complex numbers or numeric data types
        numbers = [x.real if isinstance(x, complex) else x for x in numbers if isinstance(x, (int, float, complex))]

        if len(numbers) == 0:
            return None

        numbers.sort()
        
        if len(numbers) % 2 == 0:
            return (numbers[len(numbers) // 2 - 1] + numbers[len(numbers) // 2]) / 2
        else:
            return numbers[len(numbers) // 2]
    
    except (TypeError, ValueError) as e:
        print(f"An error occurred: {e}")