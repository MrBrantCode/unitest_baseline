"""
QUESTION:
Create a function called `findRareFruits` that takes a list of fruit names as input, returns a list of unique fruit names that appear only once in the input list, excluding those that start with the letters 'a' or 'b', and with the first letter of each fruit name capitalized. The returned list should be sorted in descending order.
"""

def findRareFruits(fruitList):
    return sorted([word.capitalize() for word in set(fruitList) if fruitList.count(word) == 1 and not word.lower().startswith(('a', 'b'))], reverse=True)