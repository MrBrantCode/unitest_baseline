"""
QUESTION:
Write a function called `transform_table_data` that takes a 2D list `table_data` as input, where each inner list represents a row in the table with two elements: name and amount. The function should return a list of two lists: the first list contains the names, and the second list contains the corresponding amounts, both in the same order as they appeared in the input table. The function should assume that the input table data is valid and does not contain any errors.
"""

def transform_table_data(table_data):
    names = [row[0] for row in table_data]
    amounts = [row[1] for row in table_data]
    return [names, amounts]