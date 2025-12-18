"""
QUESTION:
Create a function `generate_nickname` that takes three parameters: `name`, `birth_year`, and `favorite_color`, and returns a unique nickname. The nickname should be a combination of the first two letters of the `name`, the last two digits of the `birth_year`, and the first two letters of the `favorite_color`. The function should be able to handle string inputs for `name` and `favorite_color`, and an integer input for `birth_year`.
"""

def generate_nickname(name, birth_year, favorite_color):
    nickname = name[:2] + str(birth_year)[-2:] + favorite_color[:2]
    return nickname