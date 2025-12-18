"""
QUESTION:
Create a function named `check_divisibility(num1, num2)` that checks whether two positive integers are divisible by each other without using built-in division operators. The function should return "Divisible" if `num1` is divisible by `num2`, "Not Divisible" otherwise. If both numbers are zero, or either number is negative or not an integer, the function should print "Invalid Input". Additionally, the function should handle the case where `num1` equals `num2` and print "Invalid Input" to avoid division by zero. The function should be able to handle large numbers efficiently.
"""

def check_divisibility(num1, num2):
    # Check if both numbers are zero
    if num1 == 0 and num2 == 0:
        return "Invalid Input"
    
    # Check if either number is negative or not an integer
    if type(num1) != int or type(num2) != int or num1 < 0 or num2 < 0:
        return "Invalid Input"
    
    # Check if both numbers are equal
    if num1 == num2:
        return "Invalid Input"
    
    # Check divisibility without using built-in division operators
    while num1 >= num2:
        num1 -= num2
    
    if num1 == 0:
        return "Divisible"
    else:
        return "Not Divisible"