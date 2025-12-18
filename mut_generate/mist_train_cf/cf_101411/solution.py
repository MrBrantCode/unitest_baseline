"""
QUESTION:
Write a function `calculate_total_income` that takes a list of employee dictionaries as input, where each dictionary contains the keys "gender", "education", "age", "hours_worked", "years_of_experience", "last_bonus_month", and "income". The function should return the total income of employees who are male, have a college degree, are between 25 and 30 years old, work more than 40 hours a week, have at least 2 years of experience, and have not received a bonus in the current month.
"""

def calculate_total_income(employees):
    total_income = 0
    for employee in employees:
        if employee["gender"] == "male" and employee["education"] == "college" and 25 <= employee["age"] <= 30 and employee["hours_worked"] > 40 and employee["years_of_experience"] >= 2 and employee["last_bonus_month"] != "current":
            total_income += employee["income"]
    return total_income