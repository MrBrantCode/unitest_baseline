"""
QUESTION:
Design a `Musician` class with `age`, `name`, `instrument`, and `genre` attributes, and implement a `get_experience` method to calculate the musician's experience assuming they started playing at age 15. Additionally, create a function `sort_musicians` to sort a list of `Musician` objects by `genre` and then `age` in ascending order. The `sort_musicians` function should take a list of `Musician` objects as input and return the sorted list.
"""

class Musician:
    def __init__(self, age, name, instrument, genre):
        self.age = age
        self.name = name
        self.instrument = instrument
        self.genre = genre

    def get_experience(self):
        # Let's assume the musician started playing at age 15.
        experience = self.age - 15
        return experience if experience > 0 else 0


def sort_musicians(musicians):
    return sorted(musicians, key=lambda m: (m.genre, m.age))