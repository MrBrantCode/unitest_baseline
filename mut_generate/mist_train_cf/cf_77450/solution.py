"""
QUESTION:
Write a function `calculate_bmi` that takes a dictionary representing a person with keys "weight" and "height" and their corresponding values as strings including units ("kg" and "m" respectively). The function should correctly calculate the body mass index (BMI) by first converting the weight and height to numerical values and then performing the BMI calculation. Assume the input dictionary may contain other irrelevant keys.
"""

def calculate_bmi(person):
    """
    Calculate the body mass index (BMI) from a person's weight and height.

    Args:
    person (dict): A dictionary representing a person with keys "weight" and "height" 
                   and their corresponding values as strings including units ("kg" and "m" respectively).

    Returns:
    float: The calculated BMI.
    """

    # Remove 'kg' from 'weight' and 'm' from 'height' and convert the result to float
    weight = float(person["weight"].replace("kg", ""))
    height = float(person["height"].replace("m", ""))

    # Calculate BMI
    bmi = weight / (height ** 2)
    return bmi