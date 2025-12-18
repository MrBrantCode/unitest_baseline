"""
QUESTION:
Create a function `check_parity(numbers)` that accepts a list of integers and returns a list of strings where each string represents whether the corresponding number in the input list is even or odd. The function should avoid using recursion to prevent exceeding the maximum recursion limit for large inputs.
"""

def check_parity(numbers):
    messages = []
    
    for num in numbers:
        if num % 2 == 0:
            msg = f"The number {num} is even."
        else:
            msg = f"The number {num} is odd."
            
        messages.append(msg)
    
    return messages