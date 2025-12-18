"""
QUESTION:
Create a function called `fruits_in_basket` that takes two parameters: `basket_size` (the total weight of the basket) and `ratio` (a list of integers representing the ratio of different types of fruits). The function should return a list of weights of each type of fruit if the given ratio and basket size are possible to achieve, otherwise it should return an error message. The function should be able to handle any number of fruit types and any basket size. The weights of the fruits should be in the same order as their corresponding ratios.
"""

def fruits_in_basket(basket_size, ratio):
    total_ratio = sum(ratio)

    if basket_size % total_ratio != 0:
        return "Error: The given ratio and basket size are not possible to achieve"

    multiple = basket_size / total_ratio
    fruits_kg = [r * multiple for r in ratio]

    return fruits_kg