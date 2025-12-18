"""
QUESTION:
Create a function `get_rare_fruits` that takes a list of fruit names as input and returns a list of rare fruits. A rare fruit is a fruit that appears only once in the input list. The function should exclude fruits that start with the letters 'a' and 'b', capitalize the first letter of each rare fruit name, and return the list in descending order.
"""

def get_rare_fruits(fruit_list):
    return sorted([word.capitalize() for word in set(fruit_list) if fruit_list.count(word) == 1 and not word.startswith(('a', 'b', 'A', 'B'))], reverse=True)