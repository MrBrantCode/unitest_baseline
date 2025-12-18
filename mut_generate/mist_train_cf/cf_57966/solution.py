"""
QUESTION:
Create a function `generate_html_table` that takes a 2D list of strings as input where each inner list contains a single string of comma-separated values. The function should return a string representing an HTML table where each row in the table corresponds to a string in the input list, and each column corresponds to a comma-separated value in the string. The input list is guaranteed to have at least one inner list, and the first inner list contains the header row of the table.
"""

def generate_html_table(table_data):
    """
    This function generates an HTML table representation of a given 2D list.
    
    Args:
    table_data (list): A 2D list of strings where each inner list contains a single string of comma-separated values.
    
    Returns:
    str: A string representing the HTML table.
    """
    html = "<table>\n"
    
    # First, we create the header row
    html += "\t<tr>\n"
    for item in table_data[0][0].split(','):
        html += "\t\t<th>{}</th>\n".format(item.strip())
    html += "\t</tr>\n"
    
    # Then, we create the data rows
    for sublist in table_data[1:]:
        html += "\t<tr>\n"
        for item in sublist[0].split(','):
            html += "\t\t<td>{}</td>\n".format(item.strip())
        html += "\t</tr>\n"
        
    html += "</table>"
    
    return html