"""
QUESTION:
Generate a function `generate_html_table` that takes a 2D list of data as input where the first sub-list contains column headers and the rest are rows of data. The function should return an HTML string representing a table with the given data, using the first row as table headers.
"""

def generate_html_table(data):
    html = "<table>\n"
    for i, row in enumerate(data):
        html += "  <tr>\n"
        for col in row:
            if i == 0:
                html += "    <th>{}</th>\n".format(col)
            else:
                html += "    <td>{}</td>\n".format(col)
        html += "  </tr>\n"
    html += "</table>\n"
    return html