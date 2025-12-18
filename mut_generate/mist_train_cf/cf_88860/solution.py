"""
QUESTION:
Create a function `calculate_average_age` that takes a list of positive integers representing ages and returns the average age rounded to the nearest whole number, the maximum age, the minimum age, and the count of ages that are more than 10 years above or below the average age.
"""

def calculate_average_age(ages):
    total_age = 0
    max_age = float('-inf')
    min_age = float('inf')
    outlier_count = 0

    for age in ages:
        total_age += age
        max_age = max(max_age, age)
        min_age = min(min_age, age)

    average_age = round(total_age / len(ages))

    for age in ages:
        if age > average_age + 10 or age < average_age - 10:
            outlier_count += 1

    return average_age, max_age, min_age, outlier_count