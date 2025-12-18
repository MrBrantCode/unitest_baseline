"""
QUESTION:
Create a function `compare_numbers(num1, num2)` that compares two numbers and returns 'lower', 'higher', or 'equal' based on the comparison. The function should be able to handle decimal values, round them to the nearest whole number, and convert numbers in scientific notation to decimal values. The function should have a time complexity of O(1).
"""

def entrance(num1, num2):
    # Convert numbers to decimal values
    if isinstance(num1, int):
        num1 = float(num1)
    if isinstance(num2, int):
        num2 = float(num2)
        
    # Convert numbers in scientific notation to decimal values
    if isinstance(num1, str) and 'e' in num1:
        num1 = float(num1)
    if isinstance(num2, str) and 'e' in num2:
        num2 = float(num2)
        
    # Round decimal values to nearest whole number
    if isinstance(num1, float):
        num1 = round(num1)
    if isinstance(num2, float):
        num2 = round(num2)
        
    # Compare the rounded numbers
    if num1 < num2:
        return 'lower'
    elif num1 > num2:
        return 'higher'
    else:
        return 'equal'