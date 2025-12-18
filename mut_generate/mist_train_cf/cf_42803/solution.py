"""
QUESTION:
Create a function `excel_to_html_table` that takes a file path to an Excel file as input and returns an HTML string representing the data in the Excel file as a table. The function should handle the following requirements:
1. Read the data from the Excel file.
2. Generate an HTML table with the same structure as the Excel data.
3. Return the HTML string representing the table.

The Excel file is assumed to have a header row and contain only text and numeric data.
"""

import pandas as pd

def excel_to_html_table(file_path):
    try:
        data = pd.read_excel(file_path).to_dict(orient='records')
        html = "<!DOCTYPE html>\n<html lang=\"en\">\n   <head>\n      <meta charset=\"utf-8\">\n   </head>\n   <body>\n      <table>\n"
        
        # Add table headers
        html += "         <tr>\n"
        for header in data[0].keys():
            html += f"            <th>{header}</th>\n"
        html += "         </tr>\n"
        
        # Add table rows
        for row in data:
            html += "         <tr>\n"
            for value in row.values():
                html += f"            <td>{value}</td>\n"
            html += "         </tr>\n"
        
        html += "      </table>\n   </body>\n</html>"
        return html
    except Exception as e:
        return f"Error: {e}"