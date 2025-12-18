"""
QUESTION:
Write a function called `generate_nickname` that takes in three parameters: a string `name`, an integer `birth_year`, and a string `favorite_color`. The function should return a string that is a combination of the first two letters of `name`, the last two digits of `birth_year`, and the first two letters of `favorite_color`.
"""

def generate_nickname(name, birth_year, favorite_color):
    nickname = name[:2] + str(birth_year)[-2:] + favorite_color[:2]
    return nickname