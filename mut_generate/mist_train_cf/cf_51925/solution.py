"""
QUESTION:
Calculate the total income of 10 partners in a startup. Each partner earns 10% less than the one who earns more than them, and Tom, who is in the 4th position from the top, earns $5,000 per month. Write a program to calculate the total income based on these conditions using the `calculate_total_income` function.
"""

def calculate_total_income(n, tom_income):
    tom_position = 4
    highest_income = tom_income / ((0.9) ** (tom_position - 1))
    total_income = 0
    for i in range(n):
        total_income += highest_income * ((0.9) ** i)
    return total_income