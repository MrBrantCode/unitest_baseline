"""
QUESTION:
Write a Python function `generate_letter_of_recommendation` that takes the recipient's name, position/award/program, length of time worked with the candidate, candidate's professional achievements, personal qualities, work ethic and leadership abilities, your name, and your contact information as input. The function should return a formatted letter of recommendation.
"""

def generate_letter_of_recommendation(recipient_name, position, length_of_time, professional_achievements, personal_qualities, work_ethic_and_leadership_abilities, your_name, your_contact_information):
    """
    Generates a formatted letter of recommendation.

    Args:
    - recipient_name (str): The recipient's name.
    - position (str): Position/award/program the candidate is being recommended for.
    - length_of_time (str): Length of time worked with the candidate.
    - professional_achievements (str): Candidate's professional achievements.
    - personal_qualities (str): Candidate's personal qualities.
    - work_ethic_and_leadership_abilities (str): Candidate's work ethic and leadership abilities.
    - your_name (str): Your name.
    - your_contact_information (str): Your contact information.

    Returns:
    - str: A formatted letter of recommendation.
    """
    letter = f"Dear {recipient_name},\n\nI am writing to recommend John Smith for {position}. I have had the pleasure of working with John for {length_of_time} and can attest to his {professional_achievements} and {personal_qualities}. John is a {work_ethic_and_leadership_abilities}.\n\nPlease do not hesitate to contact me if you have any further questions.\n\nSincerely,\n{your_name}\n{your_contact_information}"
    return letter