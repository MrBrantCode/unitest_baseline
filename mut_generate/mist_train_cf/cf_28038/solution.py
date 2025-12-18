"""
QUESTION:
Implement the `calculate_average` method in the `CsvReader` class, which takes a `column_name` parameter and returns the average value of the specified column in the CSV data. The method should ignore non-numeric values and return 0 if the column contains no numeric values.
"""

def calculate_average(data, column_name):
    total = 0
    count = 0
    for row in data:
        if row.get(column_name).isdigit():
            total += int(row.get(column_name))
            count += 1
    if count == 0:
        return 0
    return total / count