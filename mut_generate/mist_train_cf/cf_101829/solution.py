"""
QUESTION:
Write a function called `generate_recommendation_letter` that takes in the following parameters: recipient's name, position/award/program, length of time worked with the individual, their professional achievements, personal qualities, work ethic and leadership abilities, your name, and your contact information. The function should return a formatted letter of recommendation with the given information.
"""

def generate_recommendation_letter(recipient_name, position, length_of_time, professional_achievements, personal_qualities, work_ethic_and_leadership_abilities, your_name, your_contact_info):
    """
    Generate a formatted letter of recommendation.

    Args:
    recipient_name (str): The name of the recipient.
    position (str): The position/award/program.
    length_of_time (str): The length of time worked with the individual.
    professional_achievements (str): The individual's professional achievements.
    personal_qualities (str): The individual's personal qualities.
    work_ethic_and_leadership_abilities (str): The individual's work ethic and leadership abilities.
    your_name (str): Your name.
    your_contact_info (str): Your contact information.

    Returns:
    str: A formatted letter of recommendation.
    """
    letter = f"Dear {recipient_name},\n\n"
    letter += f"I am writing to recommend John Smith for {position}. "
    letter += f"I have had the pleasure of working with John for {length_of_time} "
    letter += f"and can attest to his {professional_achievements} and {personal_qualities}. "
    letter += f"John is a {work_ethic_and_leadership_abilities}.\n\n"
    letter += "Please do not hesitate to contact me if you have any further questions.\n\n"
    letter += f"Sincerely,\n{your_name}\n{your_contact_info}"
    return letter