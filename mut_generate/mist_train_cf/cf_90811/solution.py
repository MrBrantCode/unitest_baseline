"""
QUESTION:
Create a function named `find_difference(num1, num2)` that calculates the absolute difference between two integers `num1` and `num2`. The input integers must be within the range of -1000 to 1000. The function should return the absolute difference rounded to the nearest whole number. If either of the input integers is outside the specified range, the function should return `None`.
"""

def find_difference(num1, num2):
    # Check if the numbers are within the range of -1000 to 1000
    if -1000 <= num1 <= 1000 and -1000 <= num2 <= 1000:
        # Calculate the absolute difference
        diff = abs(num1 - num2)
        # Round the difference to the nearest whole number
        rounded_diff = round(diff)
        # Return the rounded difference
        return rounded_diff
    else:
        # If the numbers are not within the range, return None
        return None