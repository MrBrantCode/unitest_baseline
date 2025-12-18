"""
QUESTION:
Create a function named `restructure_data` that takes a dictionary containing lists of names, ages, occupations, and languages. Restructure this data into a list of dictionaries where each dictionary represents an individual's information, including their name, age, occupation, and language. Ensure that only individuals between the ages of 20 and 40 (exclusive) are included in the output. The input dictionary's lists are assumed to be the same length and correctly aligned.
"""

def restructure_data(data):
    """
    Restructure data from a dictionary of lists into a list of dictionaries.
    
    Args:
        data (dict): Dictionary containing lists of names, ages, occupations, and languages.
    
    Returns:
        list: List of dictionaries where each dictionary represents an individual's information.
    """
    return [{"name": data["names"][i], "age": data["ages"][i], "occupation": data["occupations"][i], "language": data["languages"][i]}
            for i in range(len(data["names"])) if 20 < data["ages"][i] < 40]