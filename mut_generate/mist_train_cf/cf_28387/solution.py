"""
QUESTION:
Create a function `create_hyperlinks` that takes a DataFrame and a column name as input. The function should return a new DataFrame with hyperlinks created from the values in the specified column. The hyperlinks should be in the format `<a href="http://url">url</a>`. Assume that the values in the specified column are valid URLs without the protocol prefix ("http://").
"""

import pandas as pd

def create_hyperlinks(dataframe, column_name):
    def make_hyperlink(url):
        return f'<a href="http://{url}">{url}</a>'
    
    dataframe[column_name] = dataframe[column_name].apply(make_hyperlink)
    return dataframe