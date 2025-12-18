"""
QUESTION:
Write a function named `calculate_average_age` that calculates the average age of people from a given list of tuples. The function should expect a list of tuples as input, where each tuple represents a person and contains exactly 20 elements. The tuple should be in the format (name, age, gender, occupation, salary, has_car, nationality, favorite_color, favorite_food, favorite_animal, ...). The function should skip any tuples that do not meet this format or have an age outside the range of 18 to 70. The function should return the average age of the valid tuples, rounded to the nearest whole number. If no valid tuples are found, the function should return 0.
"""

def calculate_average_age(tuples):
    valid_tuples = [t for t in tuples if len(t) == 20 and isinstance(t[1], int) and 18 <= t[1] <= 70]
    return round(sum(t[1] for t in valid_tuples) / len(valid_tuples)) if valid_tuples else 0