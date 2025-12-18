"""
QUESTION:
Write a function named `recommended_sleep_hours` that takes in two parameters: `age` and `gender`. The function should return the recommended hours of sleep per night based on the National Sleep Foundation's guidelines, which vary by age but not by gender. The function should return a string representing the recommended sleep range. Assume that the input age is a non-negative integer and the input gender is either 'male' or 'female'.
"""

def recommended_sleep_hours(age, gender):
    if age >= 18 and age <= 64:
        return '7-9 hours'
    elif age >= 65:
        return '7-8 hours'
    elif age >= 14 and age <= 17:
        return '8-10 hours'
    elif age >= 6 and age <= 13:
        return '9-11 hours'
    elif age >= 3 and age <= 5:
        return '10-13 hours'
    elif age >= 1 and age <= 2:
        return '11-14 hours'
    else:
        return '14-17 hours'