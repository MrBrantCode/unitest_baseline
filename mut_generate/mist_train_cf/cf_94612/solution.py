"""
QUESTION:
Create a function named `unpack_and_calculate_average_age` that takes a list of tuples as input and returns the average age of the people in the tuples. Each tuple should contain exactly 10 elements: name (string), age (integer), gender (string), occupation (string), salary (float), car ownership (boolean), nationality (string), favorite color (string), favorite food (string), and favorite animal (string). The age should be between 18 and 60 (inclusive), and names should be unique. The function should skip any tuples that do not meet these criteria and return the average age rounded to the nearest whole number. If no valid tuples are found, the function should return 0.
"""

def unpack_and_calculate_average_age(tuples):
    """
    Calculate the average age of people from a list of tuples.

    Args:
        tuples (list): A list of tuples containing information about people.
            Each tuple should contain exactly 10 elements: name (string), age (integer), 
            gender (string), occupation (string), salary (float), car ownership (boolean), 
            nationality (string), favorite color (string), favorite food (string), and 
            favorite animal (string).

    Returns:
        int: The average age of the people in the tuples, rounded to the nearest whole number.
            If no valid tuples are found, returns 0.
    """

    valid_tuples = []
    total_age = 0

    for tup in tuples:
        if len(tup) != 10:
            continue

        name = tup[0]
        age = tup[1]
        gender = tup[2]
        occupation = tup[3]
        salary = tup[4]
        has_car = tup[5]
        nationality = tup[6]
        favorite_color = tup[7]
        favorite_food = tup[8]
        favorite_animal = tup[9]

        if not isinstance(name, str) or \
                not isinstance(age, int) or \
                not isinstance(gender, str) or \
                not isinstance(occupation, str) or \
                not isinstance(salary, float) or \
                not isinstance(has_car, bool) or \
                not isinstance(nationality, str) or \
                not isinstance(favorite_color, str) or \
                not isinstance(favorite_food, str) or \
                not isinstance(favorite_animal, str):
            continue

        if not (18 <= age <= 60):
            continue

        valid_tuples.append(tup)
        total_age += age

    if len(valid_tuples) == 0:
        return 0

    average_age = round(total_age / len(valid_tuples))
    return average_age