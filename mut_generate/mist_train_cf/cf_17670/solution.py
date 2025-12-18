"""
QUESTION:
Write a Python function named `generate_html_table` that takes a dictionary as input where each key-value pair represents a field and value of student information. The function should return a string of HTML code representing a table with the following properties: 
- A 1-pixel solid black border.
- A caption that says "Student Information".
- A table header row with a light gray background color and "Field" and "Value" as column headers.
- Each data row should have an alternating background color of light blue and white.
- The font size of the table should be 12 pixels.
"""

def generate_html_table(student_info):
    table_html = "<table style='border: 1px solid black; font-size: 12px;'>"
    table_html += "<caption>Student Information</caption>"
    table_html += "<tr style='background-color: lightgray;'><th>Field</th><th>Value</th></tr>"
    
    row_count = 0
    for field, value in student_info.items():
        row_color = "lightblue" if row_count % 2 == 0 else "white"
        table_html += f"<tr style='background-color: {row_color};'><td>{field}</td><td>{value}</td></tr>"
        row_count += 1
    
    table_html += "</table>"
    
    return table_html