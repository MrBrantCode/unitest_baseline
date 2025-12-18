"""
QUESTION:
Implement a function named `sort_table` that sorts a given table in ascending order based on the "Value" column. The table is represented as a dictionary with two keys: "Index" and "Value". The function should return the sorted table as a dictionary. The function should only use the bubble sort algorithm and should not use any built-in sorting functions.
"""

def sort_table(table):
    n = len(table)
    for i in range(n):
        for j in range(0, n-i-1):
            if table['Value'][j] > table['Value'][j+1]:
                # swap the values in the "Value" column
                table.at[j, 'Value'], table.at[j+1, 'Value'] = table.at[j+1, 'Value'], table.at[j, 'Value']
                # swap the corresponding values in the "Index" column
                table.at[j, 'Index'], table.at[j+1, 'Index'] = table.at[j+1, 'Index'], table.at[j, 'Index']
    return table