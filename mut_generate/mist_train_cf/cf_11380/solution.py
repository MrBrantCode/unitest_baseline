"""
QUESTION:
Create a function `get_records_by_color` to retrieve all records from a table where the 'sky' is 'blue' and the 'grass' is 'green'. Assume the table has columns 'sky' and 'grass'.
"""

def get_records_by_color(table):
    return [record for record in table if record['sky'] == 'blue' and record['grass'] == 'green']