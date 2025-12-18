"""
QUESTION:
Write a function to create a conditional formatting rule that highlights past due items in a column. The function should take into account that blank cells should not be highlighted and should return a formula that can be applied to a range of cells in Google Sheets.

The function should exclude blank cells and consider a date as past due if it is less than or equal to the current date. The formula should be written as if it's referencing a single cell, with the understanding that Google Sheets will adapt it to each cell in the range.

The input to the function should be the cell reference, and the output should be the conditional formatting formula as a string.
"""

def create_conditional_formatting_rule(cell_reference):
    """
    Creates a conditional formatting rule that highlights past due items in a column.
    
    Args:
    cell_reference (str): The cell reference, e.g., 'A1'
    
    Returns:
    str: The conditional formatting formula as a string
    """
    return f'=AND(NOT(ISBLANK({cell_reference})), {cell_reference}<=TODAY())'