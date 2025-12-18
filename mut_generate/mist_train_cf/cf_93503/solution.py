"""
QUESTION:
Write a function `generate_html_table` that takes a list of dictionaries as input where each dictionary contains 'name' and 'age' keys representing a person. The function should return an HTML table string with a border, a caption "Person Details", and alternating row background colors (light grey and white). The table should only include people whose age is greater than or equal to 18.
"""

def generate_html_table(persons):
    html = "<table style='border-collapse: collapse;'>"
    html += "<caption>Person Details</caption>"
    html += "<tr><th>Name</th><th>Age</th></tr>"

    for i, person in enumerate(persons):
        if person['age'] >= 18:
            row_color = "lightgrey" if i % 2 == 0 else "white"
            html += f"<tr style='background-color: {row_color};'><td>{person['name']}</td><td>{person['age']}</td></tr>"

    html += "</table>"
    return html