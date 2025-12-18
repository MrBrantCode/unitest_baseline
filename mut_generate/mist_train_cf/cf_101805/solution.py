"""
QUESTION:
Generate a function named `generate_nickname` that takes three parameters: a person's name (string), their birth year (int), and their favorite color (string). The function should return a unique nickname by combining the first two letters of the person's name, the last two digits of their birth year, and the first two letters of their favorite color.
"""

def generate_nickname(name, birth_year, favorite_color):
    nickname = name[:2] + str(birth_year)[-2:] + favorite_color[:2]
    return nickname