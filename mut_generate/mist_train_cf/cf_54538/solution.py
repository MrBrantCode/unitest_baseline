"""
QUESTION:
Write a function `extract_lang_names` that takes a list of mixed data types as input, extracts all string elements, and returns a list of tuples where each tuple contains the extracted string and its length. The function should handle potential TypeError exceptions if the input is not a list.
"""

def extract_lang_names(lst):
    try:
        return [(i, len(i)) for i in lst if isinstance(i, str)]
    except TypeError:
        print("The input data is not a list.")
        return []