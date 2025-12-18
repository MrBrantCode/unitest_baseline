"""
QUESTION:
Create a function called `convert_json_to_html_table` that takes a JSON object containing different categories as keys and lists of items as values. The function should convert the JSON object into an HTML table, adding a 'Count' column that displays the total number of items in each row. If a category does not have an item in a particular row, the cell should display 'None' and not be counted.
"""

import json
import pandas as pd

def convert_json_to_html_table(json_object):
    """
    This function takes a JSON object containing different categories as keys and lists of items as values.
    It converts the JSON object into an HTML table, adding a 'Count' column that displays the total number of items in each row.
    If a category does not have an item in a particular row, the cell displays 'None' and is not counted.
    """
    # Convert json object to panda DataFrame
    df = pd.DataFrame.from_dict(json_object, orient='index')
    
    # Transpose the datafarme
    transposed_df = df.transpose()
    
    # Add a column of count
    transposed_df['Count'] = transposed_df.count(axis=1)
    
    # Convert to html
    html_table = transposed_df.to_html()
    
    return html_table