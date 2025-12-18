"""
QUESTION:
Write a function `count_gender_answers` that takes in a 2D list of data where each sublist represents a person's information with the first element as their gender ('Male' or 'Female') and the second element as their answer. The function should return a dictionary with two keys: 'Male' and 'Female', each containing the count of people of that gender who answered 'Biking / Cycling'.
"""

def count_gender_answers(data):
    """
    This function takes in a 2D list of data where each sublist represents a person's information 
    with the first element as their gender ('Male' or 'Female') and the second element as their answer.
    It returns a dictionary with two keys: 'Male' and 'Female', each containing the count of people 
    of that gender who answered 'Biking / Cycling'.

    Args:
        data (list): A 2D list of person's information.

    Returns:
        dict: A dictionary with the count of people of each gender who answered 'Biking / Cycling'.
    """
    # Initialize a dictionary to store the count of people of each gender who answered 'Biking / Cycling'
    gender_count = {'Male': 0, 'Female': 0}

    # Iterate over each person's information in the data
    for person in data:
        # Check if the person's answer is 'Biking / Cycling'
        if person[1] == 'Biking / Cycling':
            # Increment the count of the person's gender
            gender_count[person[0]] += 1

    # Return the dictionary with the count of people of each gender who answered 'Biking / Cycling'
    return gender_count