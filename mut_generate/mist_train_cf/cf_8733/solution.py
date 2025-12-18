"""
QUESTION:
Create a function `validateForm()` that checks the validity of user input in a form. The function should validate the following: 
- The name is at least 2 characters long and does not contain any numbers or special characters.
- The age is within a specific range, which is dynamically updated based on the selected gender. For males, the age range is 20-60, for females, it's 18-55, and for others, it's 18-65.
- The age is divisible by 5.
- If all inputs are valid, display a success message with the user's name, age, and gender, and clear the input fields.
- If any input is invalid, display an error message and disable the submit button.
"""

def validate_form(name, age, gender):
    """
    Validate the user input in a form.

    Args:
        name (str): The user's name.
        age (int): The user's age.
        gender (str): The user's gender.

    Returns:
        tuple: A tuple containing a boolean indicating whether the form is valid and a message.
    """

    # Define the age range based on the selected gender
    if gender == "male":
        age_range = (20, 60)
    elif gender == "female":
        age_range = (18, 55)
    else:
        age_range = (18, 65)

    # Initialize error and success messages
    error_message = ""
    success_message = ""

    # Check if the name is valid
    if len(name) < 2 or not name.isalpha():
        error_message += "Invalid name. "

    # Check if the age is valid
    if age < age_range[0] or age > age_range[1] or age % 5 != 0:
        error_message += "Invalid age. "

    # Return the result
    if error_message:
        return False, error_message
    else:
        success_message = f"Success! Name: {name}, Age: {age}, Gender: {gender}"
        return True, success_message