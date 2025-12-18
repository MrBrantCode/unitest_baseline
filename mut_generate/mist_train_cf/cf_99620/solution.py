"""
QUESTION:
Create a function named `generate_nickname` that takes three parameters: `george_name` (string), `birth_year` (int), and `favorite_color` (string). The function should return a string that combines the first two letters of `george_name`, the last two digits of `birth_year`, and the first two letters of `favorite_color`.
"""

def generate_nickname(george_name, birth_year, favorite_color):
    nickname = george_name[:2] + str(birth_year)[-2:] + favorite_color[:2]
    return nickname