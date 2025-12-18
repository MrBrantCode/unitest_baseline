"""
QUESTION:
Write a function named `generate_letter_of_recommendation` that takes the following parameters: 
`recipient`, `position`, `length_of_time`, `professional_achievements`, `personal_qualities`, `work_ethic_and_leadership_abilities`, `your_name`, and `your_contact_info`. The function should return a string representing a letter of recommendation.
"""

def generate_letter_of_recommendation(recipient, position, length_of_time, professional_achievements, personal_qualities, work_ethic_and_leadership_abilities, your_name, your_contact_info):
    return f"Dear {recipient},\n\nI am writing to recommend John Smith for {position}. I have had the pleasure of working with John for {length_of_time} and can attest to his {professional_achievements} and {personal_qualities}. John is a {work_ethic_and_leadership_abilities}.\n\nPlease do not hesitate to contact me if you have any further questions.\n\nSincerely,\n{your_name}\n{your_contact_info}"