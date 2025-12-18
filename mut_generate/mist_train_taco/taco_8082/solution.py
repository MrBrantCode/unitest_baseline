"""
QUESTION:
Ask a small girl - "How old are you?". She always says strange things... Lets help her!


For correct answer program should return int from 0 to 9.

Assume test input string always valid and may look like 
"1 year old" or "5 years old", etc.. The first char is number only.
"""

def extract_age(age_str: str) -> int:
    """
    Extracts the age from a string in the format "X year(s) old".

    Parameters:
    age_str (str): The input string containing the age information.

    Returns:
    int: The extracted age as an integer.
    """
    return int(age_str[0])