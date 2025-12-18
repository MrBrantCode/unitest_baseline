"""
QUESTION:
Create a function called `convert_list_to_dict` that takes a list with alternating elements, where each group of three elements represents a person's name (string type), age (string type), and hobby (string type), in that order. Convert this list into a dictionary where names are keys and values are nested dictionaries with 'Age' and 'Hobby' as keys and respective pairs as their values. The function should handle long lists efficiently.
"""

def convert_list_to_dict(input_list):
    output_dict = {}
    for i in range(0, len(input_list), 3): 
        output_dict[input_list[i]] = {'Age': input_list[i+1], 'Hobby': input_list[i+2]}
    return output_dict