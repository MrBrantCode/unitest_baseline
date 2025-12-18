"""
QUESTION:
Write a Python function called `generate_recommendation_letter` to automate the process of writing a personal letter of recommendation. The function should take in the following parameters: `recipient`, `position`, `length_of_time`, `professional_achievements`, `personal_qualities`, `work_ethic_and_leadership_abilities`, `your_name`, and `your_contact_information`. The function should return a string representing the generated letter.
"""

def generate_recommendation_letter(recipient, position, length_of_time, professional_achievements, personal_qualities, work_ethic_and_leadership_abilities, your_name, your_contact_information):
    """
    This function generates a letter of recommendation based on the provided parameters.

    Args:
    recipient (str): The recipient of the letter.
    position (str): The position the person is being recommended for.
    length_of_time (str): The length of time the recommender has known the person.
    professional_achievements (str): The person's professional achievements.
    personal_qualities (str): The person's personal qualities.
    work_ethic_and_leadership_abilities (str): The person's work ethic and leadership abilities.
    your_name (str): The name of the recommender.
    your_contact_information (str): The contact information of the recommender.

    Returns:
    str: A string representing the generated letter.
    """

    letter = f"Dear {recipient},\n\nI am writing to recommend John Smith for {position}. I have had the pleasure of working with John for {length_of_time} and can attest to his {professional_achievements} and {personal_qualities}. John is a {work_ethic_and_leadership_abilities}.\n\nPlease do not hesitate to contact me if you have any further questions.\n\nSincerely,\n{your_name}\n{your_contact_information}"
    
    return letter