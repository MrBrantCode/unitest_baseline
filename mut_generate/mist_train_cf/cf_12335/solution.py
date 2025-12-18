"""
QUESTION:
Create a function `reorganize_ages` that takes a dictionary where keys are names and values are ages. The function should return a dictionary where keys are ages and values are lists of names. The returned dictionary should be able to handle duplicate age values by storing multiple names in the same list.
"""

def reorganize_ages(name_age_dict):
    """
    Reorganize a dictionary where keys are names and values are ages into a dictionary 
    where keys are ages and values are lists of names.

    Args:
        name_age_dict (dict): A dictionary with names as keys and ages as values.

    Returns:
        dict: A dictionary with ages as keys and lists of names as values.
    """

    age_name_dict = {}
    for name, age in name_age_dict.items():
        if age in age_name_dict:
            age_name_dict[age].append(name)
        else:
            age_name_dict[age] = [name]
    return age_name_dict