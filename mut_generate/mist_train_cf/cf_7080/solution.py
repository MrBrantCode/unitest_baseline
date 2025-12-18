"""
QUESTION:
Write a function `calculate_grade(percentage)` that calculates a student's grade based on their percentage score, and `calculate_discount(price, discount_percentage)` that calculates the discounted price after applying a discount percentage. Implement the functions to achieve higher levels of statement and branch coverage in software testing. The `calculate_grade` function should return a grade based on the following criteria: A (>=90%), B (>=80%), C (>=70%), D (<70%). The `calculate_discount` function should return the discounted price if the price is greater than or equal to 0, otherwise return 0.
"""

def calculate_grade(percentage):
    if percentage >= 90:
        grade = "A"
    elif percentage >= 80:
        grade = "B"
    elif percentage >= 70:
        grade = "C"
    else:
        grade = "D"
    
    return grade

def calculate_discount(price, discount_percentage):
    if price >= 0:
        discounted_price = price - (price * discount_percentage / 100)
    else:
        discounted_price = 0
    
    return discounted_price