"""
QUESTION:
Write a function `unpack_and_calculate_average_age` that takes a list of tuples as input and returns the average age of people in the valid tuples. Each tuple should contain 10 elements: name (string), age (integer between 18 and 60), gender (string), occupation (string), salary (float), has_car (boolean), nationality (string), favorite_color (string), favorite_food (string), and favorite_animal (string). Tuples that do not meet these criteria should be skipped. The average age should be rounded to the nearest whole number.
"""

def unpack_and_calculate_average_age(tuples):
    """
    Calculate the average age of people in valid tuples.

    Args:
        tuples (list): A list of tuples, each containing 10 elements.

    Returns:
        int: The average age rounded to the nearest whole number.
    """

    valid_tuples = []
    total_age = 0

    for tup in tuples:
        if len(tup) != 10:
            continue

        name, age, gender, occupation, salary, has_car, nationality, favorite_color, favorite_food, favorite_animal = tup

        if not (isinstance(name, str) and 
                isinstance(age, int) and 
                isinstance(gender, str) and 
                isinstance(occupation, str) and 
                isinstance(salary, (int, float)) and 
                isinstance(has_car, bool) and 
                isinstance(nationality, str) and 
                isinstance(favorite_color, str) and 
                isinstance(favorite_food, str) and 
                isinstance(favorite_animal, str)):
            continue

        if not (18 <= age <= 60):
            continue

        valid_tuples.append(tup)
        total_age += age

    if len(valid_tuples) == 0:
        return 0

    average_age = round(total_age / len(valid_tuples))
    return average_age