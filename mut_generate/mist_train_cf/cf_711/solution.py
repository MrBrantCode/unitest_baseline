"""
QUESTION:
Create a class with an initialization method that takes two integers and sets them as class variables. Implement a method `calculate_sum` that calculates the sum of these two integers using only bitwise operators and logical operators, with a time complexity of O(1). Additionally, implement a method `is_even` that checks if the sum is an even number using only bitwise operators and logical operators, also with a time complexity of O(1).
"""

def calculate_sum_and_check_evenness(num1: int, num2: int) -> int:
    """Calculates the sum of two integers using only bitwise operators and logical operators, 
    and checks if the sum is even."""
    
    # Calculate the sum using bitwise operators
    while num2 != 0:
        carry = num1 & num2
        num1 = num1 ^ num2
        num2 = carry << 1

    # Check if the sum is even using bitwise operators
    is_even = (num1 & 1) == 0
    
    return num1, is_even