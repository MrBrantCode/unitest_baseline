"""
QUESTION:
Create a function called `generate_html_table` that takes in a dictionary `student_info`. The function should return an HTML table with the following properties: 
- the table has a border of 1 pixel and font size of 12 pixels,
- the table headers (Field and Value) have a background color of light gray,
- each row in the table has a background color of alternating light blue and white,
- the table has a caption that says "Student Information".
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