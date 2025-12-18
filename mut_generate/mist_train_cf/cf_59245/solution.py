"""
QUESTION:
Create a function `process_table` that takes three parameters: a 2D list `data`, a list of column indices `columns`, and a sorting column index `sort_column`. The function should return a new table containing only the specified columns, sorted in descending order based on the values in the sorting column. If there are ties in the sorting column, the rows should be sorted by the second column in ascending order. The function should handle cases where the input list of column indices contains indices that are not in the data, the input list of column indices is empty, the input sorting column index is not in the data, and the input sorting column index is not in the specified columns.
"""

def process_table(data, columns, sort_column):
    if not columns or not (0 <= sort_column < len(data[0])): 
        return "Invalid inputs"
      
    if sort_column not in columns:
        columns.append(sort_column)
        
    columns.sort() # as required by the sorting condition for ties
        
    new_data = [[data[i][j] for j in columns] for i in range(len(data))]
    new_sort_column = columns.index(sort_column)

    new_data = sorted(new_data, key=lambda row: (-int(row[new_sort_column]), row[1]))
    return new_data