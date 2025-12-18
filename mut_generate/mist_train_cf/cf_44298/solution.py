"""
QUESTION:
Write a function `calculate_mode` that takes a list of 7 elements as input and returns the mode(s) of the list. The mode is the element(s) that appears most frequently in the list. If there is no repeated element, return "No mode found".
"""

from collections import Counter

def calculate_mode(list_7):
    data = Counter(list_7)
    data_dict = dict(data)
    
    max_value = max(list(data.values()))
    mode_val = []
    
    if max_value == 1:
        return "No mode found"

    for num, freq in data_dict.items():
        if freq == max_value:
            mode_val.append(num)
    return mode_val