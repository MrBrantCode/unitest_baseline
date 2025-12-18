"""
QUESTION:
Create a function `categorize_fruits` that takes a list of fruit names and returns a dictionary where each key is a fruit name and its corresponding value is another dictionary containing the fruit's characteristics: color, taste, size, and origin. Assume the fruit characteristics are predefined and the list of fruits only contains "Apple", "Orange", "Grapes", "Bananas", and "Watermelons".
"""

def categorize_fruits(fruits):
    characteristics = {
        "Apple": {"color": "red", "taste": "sweet", "size": "medium", "origin": "domestic"},
        "Orange": {"color": "orange", "taste": "sweet and tangy", "size": "medium", "origin": "imported"},
        "Grapes": {"color": "green/purple", "taste": "sweet", "size": "small", "origin": "imported"},
        "Bananas": {"color": "yellow", "taste": "sweet", "size": "medium", "origin": "imported"},
        "Watermelons": {"color": "green", "taste": "sweet and juicy", "size": "large", "origin": "domestic"}
    }
    
    return {fruit: characteristics[fruit] for fruit in fruits}