"""
QUESTION:
Write a SQL query that sorts a table's data by two columns, 'column1' in ascending order and 'column2' in descending order, excluding rows where 'column3' is less than 10 and removing any duplicate rows. The function should return the sorted and filtered data.
"""

def sort_table(data):
    return sorted(set((row['column1'], row['column2']) for row in data if row['column3'] >= 10), key=lambda x: (x[0], -x[1]))