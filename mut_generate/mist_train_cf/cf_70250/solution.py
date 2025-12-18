"""
QUESTION:
Create a function named `convert_list_to_dict` that takes a list of lists as input, where each sublist contains at least two elements. The function should return a dictionary where the first element of each sublist is used as the key, and the remaining elements are used as the value. The function should achieve this using dictionary comprehension and maintain both time and space efficiency.
"""

def convert_list_to_dict(list_of_data):
    return {item[0]: item[1:] for item in list_of_data}