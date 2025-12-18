"""
QUESTION:
Create a function `categorize_characters` that categorizes characters based on the Myers-Briggs Type Indicator (MBTI) personality types and assigns different levels of laziness to the characters. The function should take a list of tuples containing the character's name and MBTI type as input and return a list of character objects with unique personality types and corresponding laziness levels.
"""

class Character:
    def __init__(self, name, mbti_type, laziness_level):
        self.name = name
        self.mbti_type = mbti_type
        self.laziness_level = laziness_level

def categorize_characters(characters):
    """
    Categorize characters based on their MBTI personality types and assign different levels of laziness.

    Args:
        characters (list): A list of tuples containing the character's name and MBTI type.

    Returns:
        list: A list of Character objects with unique personality types and corresponding laziness levels.
    """

    # Define the laziness levels for each personality type
    laziness_levels = {
        'INTJ': 5, 'ESFP': 9, 'ISTP': 7, 'ENFJ': 3, 'INFP': 8, 'ESTJ': 2, 'ISFJ': 6, 'ENTP': 4
    }

    # Create a list to store unique character objects
    unique_characters = []

    # Iterate over the input characters
    for name, mbti_type in characters:
        # Check if the character already exists in the list
        existing_character = next((char for char in unique_characters if char.mbti_type == mbti_type), None)

        # If the character does not exist, create a new Character object and add it to the list
        if existing_character is None:
            laziness_level = laziness_levels.get(mbti_type, 5)  # Default laziness level is 5
            unique_characters.append(Character(name, mbti_type, laziness_level))

    return unique_characters