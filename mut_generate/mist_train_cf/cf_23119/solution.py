"""
QUESTION:
Create a function named `validateUserInput` that takes a user's name, age, and gender as inputs. The function should validate the user's input based on the following rules: 

- The age should be between 18 and 65 years old for the default case, but this range should be dynamic based on the selected gender. If the user selects "male" as their gender, the age range should be between 20 and 60 years old. If the user selects "female" as their gender, the age range should be between 18 and 55 years old.
- The name should be at least 2 characters long and only contain alphabets and spaces.

The function should return an object containing a boolean indicating whether the input is valid, and an error message if the input is not valid. If the input is valid, the error message should be an empty string. 

The function should also simulate the behavior of a submit button, which should be disabled if the input is not valid and enabled otherwise.
"""

def validate_user_input(name: str, age: int, gender: str) -> tuple:
    """
    Validates user input based on the given rules.

    Args:
    name (str): The user's name.
    age (int): The user's age.
    gender (str): The user's gender.

    Returns:
    tuple: A tuple containing a boolean indicating whether the input is valid and an error message.
    """

    # Define the age ranges for each gender
    age_ranges = {
        'male': (20, 60),
        'female': (18, 55)
    }

    # Check if the age is within the valid range for the selected gender
    if gender not in age_ranges or not age_ranges[gender][0] <= age <= age_ranges[gender][1]:
        return False, "Age should be between {} and {} years old for {}.".format(*age_ranges.get(gender, (18, 65)), gender)

    # Check if the name is at least 2 characters long and only contains alphabets and spaces
    if not name.replace(" ", "").isalpha() or len(name) < 2:
        return False, "Name should be at least 2 characters long and only contain alphabets."

    # If all checks pass, the input is valid
    return True, ""