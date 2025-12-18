"""
QUESTION:
Write a function called `extract_table_data` that takes a string representing an HTML table row as input and returns a list of the data cells contained within that row. Each data cell is enclosed within `<td>` and `</td>` tags. The function should ignore any other HTML tags or content within the row.
"""

from typing import List
import re

def extract_table_data(html_row: str) -> List[str]:
    # Use regular expression to find all data cells within the HTML row
    data_cells = re.findall(r'<td>(.*?)</td>', html_row)
    return data_cells