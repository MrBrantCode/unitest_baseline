"""
QUESTION:
Implement the `intricate_text_transformation` function, which takes a string `input_text` as input and performs the following operations: 
1. Replaces all occurrences of blank space with an underscore symbol.
2. Replaces any incidence of two or more sequential empty spaces with a hyphen.
3. Transforms all words in the string to their uppercase form.
"""

def intricate_text_transformation(input_text):
    """ 
    Given a string called input_text, the function carries out the transformations 
    including transforming text to uppercase, replacing blank spaces with underscores
    and replacing two or more sequential spaces with a hyphen. 
    """
    input_text = input_text.replace(" ", "_") # replacement of blank space with underscore
    while "__" in input_text:
        input_text = input_text.replace("__", "-") # replacement of sequential underscores with a hyphen
    return input_text.upper() # transforming all expressions to their uppercase equivalents