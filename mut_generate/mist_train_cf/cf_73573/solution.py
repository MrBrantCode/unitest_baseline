"""
QUESTION:
Define a function `relationship` that takes a pandas DataFrame `df` as input and returns a list of strings representing the type of relationship between each pair of columns in the DataFrame. The relationship types are 'one-to-one', 'one-to-many', 'many-to-one', and 'many-to-many', determined by the uniqueness of values in each column. 

The function should return all pairs of columns, including both 'Column1 Column2' and 'Column2 Column1', and each pair should be represented as a string in the format 'Column1 Column2 relationship_type'.
"""

def relationship(df):
    result = []
    columns = df.columns.to_list()

    for i in range(len(columns)):
        for j in range(len(columns)):
            if i != j:
                col1_unique = df[columns[i]].nunique()
                col2_unique = df[columns[j]].nunique()

                if col1_unique == df.shape[0] and col2_unique == df.shape[0]:
                    result.append(f'{columns[i]} {columns[j]} one-to-one')
                elif col1_unique == df.shape[0] and col2_unique < df.shape[0]:
                    result.append(f'{columns[i]} {columns[j]} one-to-many')
                elif col1_unique < df.shape[0] and col2_unique == df.shape[0]:
                    result.append(f'{columns[i]} {columns[j]} many-to-one')
                else:
                    result.append(f'{columns[i]} {columns[j]} many-to-many')

    return result