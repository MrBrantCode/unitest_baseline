"""
QUESTION:
Write a function `update_non_matching_info` to update non-matching information from Table A to Table B. The tables have two columns: 'name' and 'age'. The function should update the 'age' in Table B with the 'age' from Table A where the 'name' matches in both tables.
"""

import pandas as pd

def update_non_matching_info(table_a, table_b):
    table_b.loc[table_b['name'].isin(table_a['name']), 'age'] = table_b['name'].map(table_a.set_index('name')['age'])
    return table_b