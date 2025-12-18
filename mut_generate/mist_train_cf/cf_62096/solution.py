"""
QUESTION:
Write a function called `find_lowest_freq` that takes a dictionary as input where keys represent names and values represent their frequencies. The function should return a list of names that have the lowest frequency in the dictionary. If the input dictionary is empty, the function should return `None`.
"""

def find_lowest_freq(data):
    if not data:
        return None
    min_val = min(data.values())
    return [k for k, v in data.items() if v == min_val]