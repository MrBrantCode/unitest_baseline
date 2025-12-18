"""
QUESTION:
Create a function named `define_relation` that takes two pandas Series as input and returns a string describing the nature of their relationship (one-to-one, one-to-many, many-to-one, many-to-many). Then, create a function that uses `define_relation` to generate a DataFrame where the index and columns are column names from a given DataFrame, and the cell at row i and column j describes the relationship between column i and column j. The function should return this relationship DataFrame. The input DataFrame can have any number of columns, but the output should be a square DataFrame. The diagonal of the output DataFrame should contain NaN values.
"""

def define_relation(column1, column2):
    if len(column1.unique()) == len(column2):
        if len(column2.unique()) == len(column2):
            return 'one-to-one'
        else:
            return 'one-to-many'
    else:
        if len(column2.unique()) == len(column2):
            return 'many-to-one'
        else:
            return 'many-to-many'

def describe_column_relations(df):
    relations = pd.DataFrame(index=df.columns, columns=df.columns)
    
    for column1 in df.columns:
        for column2 in df.columns:
            if column1 == column2:
                relations.loc[column1, column2] = np.nan
            else:
                relations.loc[column1, column2] = define_relation(df[column1], df[column2])
                
    return relations