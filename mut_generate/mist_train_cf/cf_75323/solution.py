"""
QUESTION:
Write a function named `sort_mobiles` that takes a list of objects of class `Mobile` as input, sorts the list according to the 'brand' name in alphabetical order, then by 'price' in descending order, and finally by 'year' of model in ascending order. The function should return the sorted list. The `Mobile` class has attributes 'brand', 'model', 'year', and 'price'.
"""

class Mobile:
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price

def sort_mobiles(mobiles):
    return sorted(mobiles, key=lambda x: (x.brand, -x.price, x.year))