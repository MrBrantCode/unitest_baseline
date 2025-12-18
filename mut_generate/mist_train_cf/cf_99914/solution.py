"""
QUESTION:
Write a function called `generate_recommendation_letter` that takes in the following parameters: `recipient`, `position`, `length_of_time`, `professional_achievements`, `personal_qualities`, `work_ethic_and_leadership_abilities`, `your_name`, and `your_contact_information`. The function should return a string representing a personal letter of recommendation addressed to the recipient, including the specified information about the candidate, John Smith, and the recommender's contact information.
"""

def generate_recommendation_letter(recipient, position, length_of_time, professional_achievements, personal_qualities, work_ethic_and_leadership_abilities, your_name, your_contact_information):
    """
    Generates a personal letter of recommendation addressed to the recipient, 
    including the specified information about the candidate, John Smith, and 
    the recommender's contact information.

    Args:
        recipient (str): The recipient of the letter.
        position (str): The position the candidate is applying for.
        length_of_time (str): The length of time the recommender has known the candidate.
        professional_achievements (str): The candidate's professional achievements.
        personal_qualities (str): The candidate's personal qualities.
        work_ethic_and_leadership_abilities (str): The candidate's work ethic and leadership abilities.
        your_name (str): The recommender's name.
        your_contact_information (str): The recommender's contact information.

    Returns:
        str: A string representing the personal letter of recommendation.
    """
    letter = f"Dear {recipient},\n\n"
    letter += f"I am writing to recommend John Smith for {position}. "
    letter += f"I have had the pleasure of working with John for {length_of_time} "
    letter += f"and can attest to his {professional_achievements} and {personal_qualities}. "
    letter += f"John is a {work_ethic_and_leadership_abilities}.\n\n"
    letter += "Please do not hesitate to contact me if you have any further questions.\n\n"
    letter += f"Sincerely,\n{your_name}\n{your_contact_information}"
    return letter