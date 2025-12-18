"""
QUESTION:
Create a function `calc_bmi_and_sort` that takes a list of tuples, where each tuple contains the height (in centimeters) and weight (in kilograms) of an individual. The function should calculate the Body Mass Index (BMI) for each individual by dividing the weight by the square of the height, then sort the data in ascending order based on the BMI values. If multiple individuals have the same BMI value, they should be sorted in descending order based on their weights.
"""

def calc_bmi_and_sort(data):
    """
    Calculate the Body Mass Index (BMI) for each individual and sort the data in ascending order based on the BMI values.
    If multiple individuals have the same BMI value, they are sorted in descending order based on their weights.

    Args:
        data (list): A list of tuples, where each tuple contains the height (in centimeters) and weight (in kilograms) of an individual.

    Returns:
        list: A list of tuples containing the height, weight, and BMI values for each individual, sorted by BMI and weight.
    """

    # Calculate BMI for each individual and store in a list of tuples
    bmi_data = [(weight / ((height / 100) ** 2), height, weight) for height, weight in data]

    # Sort the data in ascending order based on BMI and descending order based on weight
    sorted_data = sorted(bmi_data, key=lambda x: (x[0], -x[2]))

    return sorted_data