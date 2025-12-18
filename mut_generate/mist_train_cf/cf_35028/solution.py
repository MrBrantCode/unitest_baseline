"""
QUESTION:
Write a function `calculate_salutes(hallway)` that takes a string `hallway` representing a one-dimensional office layout where each position can be occupied by an employee facing either left ("<") or right (">"). Return the total number of salutes performed when employees facing right encounter employees facing left.
"""

def calculate_salutes(hallway):
    crosses = 0
    for i, char in enumerate(hallway):
        if char == ">":
            crosses += hallway[i:].count("<")
    salutes = crosses * 2
    return salutes