"""
QUESTION:
Create a function `calculate_average_sales` that takes a CSV file path and a column name as input, reads the CSV file using pandas, calculates the average of the specified column, and returns the average value rounded to two decimal places. The function should handle exceptions for file not found and column not found, and return an appropriate message in those cases. 

The function should take two parameters: `csv_file` (string) which is the path to the CSV file, and `column_name` (string) which is the name of the column for which the average needs to be calculated.
"""

import pandas as pd

def calculate_average_sales(csv_file, column_name):
    try:
        data = pd.read_csv(csv_file)
        average = data[column_name].mean()
        return round(average, 2)
    except FileNotFoundError:
        return "File not found"
    except KeyError:
        return "Column not found"
    except Exception as e:
        return str(e)