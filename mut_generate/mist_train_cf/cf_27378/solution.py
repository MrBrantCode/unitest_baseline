"""
QUESTION:
Create a function `process_air_quality_data(out, selected_column, col_mean)` that takes a DataFrame `out`, a column name `selected_column`, and a dictionary `col_mean`. The function should create two DataFrames, `Y` and `Y_true`, where `Y_true` stores the original values and `Y` stores the processed values. For the `selected_column`, fill any missing values in `Y` with the mean value for the corresponding city and pollutant type from `col_mean`. Store the original values of the `selected_column` in `Y_true`. Return `Y` with only the `selected_column`.
"""

def process_air_quality_data(out, selected_column, col_mean):
    Y = out.copy()
    Y_true = Y[[selected_column]].copy()

    Y[selected_column] = Y.apply(lambda row: row[selected_column] if not pd.isnull(row[selected_column]) 
                                else col_mean[row['city']][selected_column], axis=1)
    
    return Y[[selected_column]]