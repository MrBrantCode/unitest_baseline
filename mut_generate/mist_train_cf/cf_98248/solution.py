"""
QUESTION:
Create a function `is_root_vegetable(vegetable)` that takes a string `vegetable` as input and returns a boolean value indicating whether the vegetable is a type of root vegetable. The function should consider different characteristics of the vegetable, such as its appearance and growth habits. It should be able to handle various types of vegetable inputs and provide accurate identification.
"""

def is_root_vegetable(vegetable):
    root_vegetables = ['carrot', 'beet', 'turnip', 'radish', 'sweet potato', 'yam']
    if vegetable.lower() in root_vegetables:
        return True
    elif 'root' in vegetable.lower() or 'tuber' in vegetable.lower():
        return True
    else:
        return False