"""
QUESTION:
Implement a function `bubble_sort_table` that takes a 2D list `table` representing an Excel table with two columns, where the first column represents the index and the second column represents the values. Sort the table in ascending order based on the values in the second column. The function should return the sorted table.

Restrictions:
- The input table is a 2D list where each inner list has exactly two elements.
- The values in the second column are integers.
- The function should use the bubble sort algorithm.
"""

def bubble_sort_table(table):
    n = len(table)
    for i in range(n):
        for j in range(0, n-i-1):
            if table[j][1] > table[j+1][1]:
                # swap the values in the second column
                table[j][1], table[j+1][1] = table[j+1][1], table[j][1]
                # swap the corresponding values in the first column
                table[j][0], table[j+1][0] = table[j+1][0], table[j][0]
    return table