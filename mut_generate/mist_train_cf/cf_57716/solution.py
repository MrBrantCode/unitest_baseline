"""
QUESTION:
Create a function called `get_optimal_fruits` that takes in the current season, a list of dietary restrictions, and a list of allergies as input. The function should return a list of 10 unique and rare fruits that are in season and comply with the given dietary restrictions and allergies. Each fruit should have attributes for its name, origin, nutritional value, taste, and source. The function should also consider the seasonality of each fruit and prioritize fruits that complement each other in a fruit salad. If less than 10 fruits are available that meet the requirements, the function should return an error message.
"""

class Fruit:
    def __init__(self, name, origin, nutritional_value, taste, season, source):
        self.name = name
        self.origin = origin
        self.nutritional_value = nutritional_value
        self.taste = taste
        self.season = season
        self.source = source

rare_fruits_list = [
    Fruit("Durian", "Southeast Asia", "High in Fiber", "Sweet and Creamy", "June-October", "Thailand"),
    Fruit("Rambutan", "Malaysia", "Rich in Vit C", "Sweet and Sour", "June-September", "Malaysia"),
    # Continue for other fruits...
]

def get_optimal_fruits(season, dietary_restrictions, allergies):
    optimal_fruits = [fruit for fruit in rare_fruits_list 
                      if fruit.season == season 
                      and fruit.name not in dietary_restrictions 
                      and fruit.name not in allergies]
    if len(optimal_fruits) < 10:
        return "Sorry, not enough rare fruits are available that meet your requirements."
    return optimal_fruits[:10]