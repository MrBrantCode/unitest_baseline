"""
QUESTION:
Create a function named `get_grade` that takes a single numeric argument `n` between 1 and 100. The function should return the corresponding alphabetic grade representation, where 90-100 corresponds to "A", 80-89 corresponds to "B", 70-79 corresponds to "C", 60-69 corresponds to "D", and below 60 corresponds to "F". If the input is outside the range of 1 to 100, the function should return "Invalid input. Please enter a number between 1 and 100."
"""

def get_grade(n):
    if n < 1 or n > 100:
        return "Invalid input. Please enter a number between 1 and 100."
    elif n >= 90:
        return "A"
    elif n >= 80:
        return "B"
    elif n >= 70:
        return "C"
    elif n >= 60:
        return "D"
    else:
        return "F"