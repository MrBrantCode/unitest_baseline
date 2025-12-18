"""
QUESTION:
Write a function `league_operations(times)` that takes a tuple `times` of football team names as input and returns a list containing two values: a list of the first five teams in alphabetical order, and the position of the team "Chapecoense" in the league table (1-indexed). The input tuple is not empty and contains unique team names, including "Chapecoense".
"""

def league_operations(times):
    first_five_alphabetical = sorted(times)[:5]
    chapecoense_position = times.index('Chapecoense') + 1
    return (first_five_alphabetical, chapecoense_position)