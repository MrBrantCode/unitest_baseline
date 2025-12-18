"""
QUESTION:
Create a function named `generate_html_table` that takes a list of dictionaries as input, where each dictionary represents a fruit with its carbohydrate content. The function should sort the fruits in descending order of their carbohydrate content and return an HTML table as a string. The HTML table should have two columns: 'Fruit' and 'Carbohydrates'. The function should use the input list as the data source for the table and return the generated HTML table.
"""

def generate_html_table(fruits):
    """
    Generate an HTML table from a list of fruits with their carbohydrate content.

    Args:
        fruits (list): A list of dictionaries, where each dictionary represents a fruit with its carbohydrate content.

    Returns:
        str: The generated HTML table as a string.
    """
    # Sort the fruits list in descending order of carbohydrate content
    sorted_fruits = sorted(fruits, key=lambda x: x['carbohydrates'], reverse=True)
    # Generate the HTML table
    html_table = "<table><tr><th>Fruit</th><th>Carbohydrates</th></tr>"
    for fruit in sorted_fruits:
        html_table += "<tr><td>{}</td><td>{}</td></tr>".format(fruit['name'], fruit['carbohydrates'])
    html_table += "</table>"
    return html_table