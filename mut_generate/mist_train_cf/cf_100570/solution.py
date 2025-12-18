"""
QUESTION:
Create a Python function named `is_root_vegetable` that takes one parameter `vegetable`. The function should determine if the given `vegetable` is a type of root vegetable based on its characteristics, such as its appearance and growth habits. The function should consider various factors, including whether the vegetable grows underground, has a taproot or fibrous roots, and has a starchy texture. The function should be able to handle various types of vegetable inputs and provide accurate identification.
"""

def is_root_vegetable(vegetable):
    root_vegetables = ['carrot', 'beet', 'turnip', 'radish', 'sweet potato', 'yam']
    if vegetable.lower() in root_vegetables:
        return True
    elif 'root' in vegetable.lower() or 'tuber' in vegetable.lower():
        return True
    else:
        return False