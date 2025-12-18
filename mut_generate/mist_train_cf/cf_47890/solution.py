"""
QUESTION:
Write a function named `fruit_salad_ratio` that calculates the ratio of the number of pears to the number of apples and oranges in a fruit salad, given that Simon initially had x pears and y apples (x + y = 12), then added 12 oranges to make a total of 24 fruits.
"""

def fruit_salad_ratio(x, y):
    # Calculate the total number of apples and oranges
    total_apples_oranges = 12 - x + 12
    
    # Calculate the ratio of pears to the number of apples and oranges
    ratio = x / total_apples_oranges
    
    return ratio