"""
QUESTION:
Write a function `matrix_to_json(matrix)` that transforms a sparse two-dimensional matrix into a JSON string, where only non-null/non-zero elements along with their indices are stored. The output format should be a list of dictionaries, each containing the row index, column index, and value of a non-null/non-zero element. The function should be efficient for large sparse matrices.
"""

import json

def matrix_to_json(matrix):
    json_out = []
    for row_idx, row in enumerate(matrix):
        for col_idx, x in enumerate(row):
            if x: # save only non-null/non-zero elements
                json_out.append({"row": row_idx, "col": col_idx, "value": x})
    return json.dumps(json_out)