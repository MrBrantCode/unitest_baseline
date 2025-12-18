"""
QUESTION:
Create a function `select_rows` to filter rows from a table based on multiple conditions. The function should take a table and select rows where the 'fruit_type' is either 'apple' or 'orange', the 'region' is either 'California' or 'Florida', and the 'quantity' is greater than 10.
"""

def select_rows(table):
    return [row for row in table if (row['fruit_type'] in ['apple', 'orange']) 
            and (row['region'] in ['California', 'Florida']) 
            and row['quantity'] > 10]