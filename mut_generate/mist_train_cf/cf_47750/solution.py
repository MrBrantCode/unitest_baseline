"""
QUESTION:
Create a function `relationship(column1, column2)` that determines the nature of the relationship between two columns in a dataframe. The function should return a string indicating whether the relationship is 'one-2-one', 'one-2-many', 'many-2-one', or 'many-2-many'. 

The function should take into account the uniqueness of values in both columns. If both columns have unique values, the relationship is 'one-2-one'. If one column has unique values and the other does not, the relationship is 'one-2-many' or 'many-2-one'. If neither column has unique values, the relationship is 'many-2-many'. 

Apply this function to all pairs of columns in a dataframe and return a list of strings in the format 'Column1 Column2 relationship'.
"""

def relationship(column1, column2):
    """
    Determine the nature of the relationship between two columns in a dataframe.

    Args:
    column1 (Series): The first column.
    column2 (Series): The second column.

    Returns:
    str: A string indicating the relationship between the columns ('one-2-one', 'one-2-many', 'many-2-one', or 'many-2-many').
    """
    if len(column1) == len(column1.unique()) and len(column2) == len(column2.unique()):
        return 'one-2-one'
    elif len(column1) == len(column1.unique()) and len(column2) != len(column2.unique()):
        return 'one-2-many'
    elif len(column1) != len(column1.unique()) and len(column2) == len(column2.unique()):
        return 'many-2-one'
    else:
        return 'many-2-many'