"""
QUESTION:
Create a function named `categorize_characters_by_personality` that categorizes characters based on their personality types according to the Myers-Briggs Type Indicator (MBTI) and assigns different levels of laziness to each character based on their personality type. Each character must have a unique personality type. The function should take a list of character names as input and return a list of characters with their corresponding personality types and laziness levels. The laziness level should be used to determine whether a character is too lazy to send a message or not.
"""

def categorize_characters_by_personality(character_names, personality_types):
    characters = []
    for name, personality in zip(character_names, personality_types):
        laziness_level = 5  # default laziness level for Introverted and Perceiving types
        if 'E' in personality and 'J' in personality:
            laziness_level = 2  # Extraverted and Judging types are less lazy
        elif 'I' in personality and 'P' in personality:
            laziness_level = 8  # Introverted and Perceiving types are lazier
        elif 'E' in personality and 'P' in personality:
            laziness_level = 4  # Extraverted and Perceiving types are moderately lazy
        else:
            laziness_level = 6  # default laziness level for other types
        characters.append({'name': name, 'mbti_type': personality, 'laziness_level': laziness_level})
    return characters