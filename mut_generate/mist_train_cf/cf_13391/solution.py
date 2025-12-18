"""
QUESTION:
Create a function `transform_list` that takes a list of tuples containing emails, names, and ages. The function should return a dictionary where the keys are the emails, the values are tuples of names and ages, and each email's length is implicitly included as part of the key. Only include emails that match the format [username]@[domain].[extension] and belong to users aged 30 or older.
"""

import re

def transform_list(my_list):
    """
    This function transforms a list of tuples containing emails, names, and ages into a dictionary.
    The dictionary's keys are the emails and its values are tuples of names and ages.
    Only emails that match the format [username]@[domain].[extension] and belong to users aged 30 or older are included.
    
    Parameters:
    my_list (list): A list of tuples containing emails, names, and ages.
    
    Returns:
    dict: A dictionary where the keys are the emails and the values are tuples of names and ages.
    """

    def validate_email(email):
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(pattern, email)

    email_dict = {}
    for email, name, age in my_list:
        if int(age) >= 30 and validate_email(email):
            email_dict[email] = (name, int(age))
    return email_dict