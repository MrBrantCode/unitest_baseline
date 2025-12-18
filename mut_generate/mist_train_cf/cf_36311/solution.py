"""
QUESTION:
Implement a function `generate_summary_report(table)` that takes a table as input, calculates the average value for each column, and returns a formatted summary report as a string. The table is a list of rows, where each row is a tuple containing a string representing the row heading and a list of tuples representing the column values. Each column tuple consists of a string column heading and a numerical value. The summary report should display the average value for each column, rounded to two decimal places, along with the corresponding column heading, formatted as follows: 

```
Summary Report:
Column Heading 1: Average Value 1
Column Heading 2: Average Value 2
...
```
"""

def generate_summary_report(table):
    summary = "Summary Report:\n"
    column_totals = {}
    column_counts = {}
    
    for row in table:
        for column_heading, value in row[1]:
            if column_heading not in column_totals:
                column_totals[column_heading] = value
                column_counts[column_heading] = 1
            else:
                column_totals[column_heading] += value
                column_counts[column_heading] += 1
    
    for column_heading, total in column_totals.items():
        average = total / column_counts[column_heading]
        summary += f"{column_heading}: {average:.2f}\n"
    
    return summary