"""
QUESTION:
Write a function `extract_fruits` that takes a tuple `t` and a list of fruit names as input, and returns a list of fruit names that are present in the tuple. The tuple can contain mixed types of elements including strings, lists, and dictionaries, and the fruit names can be found as keys or values in the dictionaries or as elements in the lists. The function should eliminate repetitive elements and return the fruit names in any order.
"""

def extract_fruits(t, fruits):
    fruit_list = set()  
    for item in t:
        if isinstance(item, str) and item in fruits:
            fruit_list.add(item)
        elif isinstance(item, list):
            for i in item:
                if i in fruits:
                    fruit_list.add(i)
        elif isinstance(item, dict):
            for key, value in item.items():
                if key in fruits:
                    fruit_list.add(key)
                if value in fruits:
                    fruit_list.add(value)
            
    return list(fruit_list)