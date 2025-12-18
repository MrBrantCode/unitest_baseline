"""
QUESTION:
Create a function `generate_table` that generates an HTML table from a given list of dictionaries and includes a row index as the first column. The table should support sorting by each column in both ascending and descending order. The function should take the following parameters:

- `data`: A list of dictionaries where each dictionary represents a row in the table.
- `sort_column`: The column to sort by. Defaults to None.
- `sort_direction`: The direction to sort in. Defaults to 'asc'.

The function should return the HTML table as a string. The table should have a class attribute of 'sortable-table'. Each column header should have an onclick event that triggers the sorting functionality.

Note: The function should not include any styling or validation.
"""

def generate_table(data, sort_column=None, sort_direction='asc'):
    """
    Generates an HTML table from a given list of dictionaries and includes a row index as the first column.
    
    Args:
        data (list): A list of dictionaries where each dictionary represents a row in the table.
        sort_column (str): The column to sort by. Defaults to None.
        sort_direction (str): The direction to sort in. Defaults to 'asc'.
    
    Returns:
        str: The HTML table as a string.
    """
    
    # Sort the data if a sort column is provided
    if sort_column is not None:
        data.sort(key=lambda x: x[sort_column], reverse=(sort_direction == 'desc'))
    
    # Create the HTML table
    html = "<table class='sortable-table'>\n"
    html += "  <thead>\n"
    html += "    <tr>\n"
    html += "      <th onclick='sortTable(\"index\")'>Index</th>\n"
    
    # Add the column headers
    for column in data[0].keys():
        html += f"      <th onclick='sortTable(\"{column}\")'>{column.capitalize()}</th>\n"
    
    html += "    </tr>\n"
    html += "  </thead>\n"
    html += "  <tbody>\n"
    
    # Add the table rows
    for index, row in enumerate(data):
        html += "    <tr>\n"
        html += f"      <td>{index + 1}</td>\n"
        for value in row.values():
            html += f"      <td>{value}</td>\n"
        html += "    </tr>\n"
    
    html += "  </tbody>\n"
    html += "</table>"
    
    return html