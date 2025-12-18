"""
QUESTION:
Implement a function `apply_filter_conditions` that takes in a dataset `data` and a filtering conditions dictionary `filters`, and returns a filtered subset of the dataset based on the provided conditions.

The `data` is a list of dictionaries where each dictionary represents a row of the dataset with column names as keys and corresponding data as values. The `filters` dictionary contains column names as keys and filtering conditions as values. Filtering conditions can be simple (e.g., equality, inequality) or complex (e.g., logical AND of multiple conditions) with the following structure:

* Top-level dictionary represents the logical OR of the conditions for different columns.
* Each key in the top-level dictionary represents a column name.
* The value corresponding to each column name is another dictionary representing the filtering condition for that column with an "operator" key and a "value" key.
* The "and" operator can be used to represent a logical AND relationship between multiple conditions for a single column with the value corresponding to the "and" key being a list of dictionaries.

Restrictions:

* 1 <= len(data) <= 1000
* The function should return a list of dictionaries representing the subset of the input dataset that satisfies the filtering conditions.
"""

from typing import List, Dict, Any

def apply_filter_conditions(data: List[Dict[str, Any]], filters: Dict[str, Any]) -> List[Dict[str, Any]]:
    def apply_condition(row, condition):
        operator = condition["operator"]
        value = condition["value"]
        if operator == "==":
            return row == value
        elif operator == "!=":
            return row != value
        elif operator == ">":
            return row > value
        elif operator == "<":
            return row < value

    def apply_and_conditions(row, conditions):
        return all(apply_condition(row, condition) for condition in conditions)

    filtered_data = []
    for row in data:
        satisfies_filters = all(
            apply_and_conditions(row.get(column_name), conditions)
            if isinstance(conditions, list)
            else apply_condition(row.get(column_name), conditions)
            for column_name, conditions in filters.items()
        )
        if satisfies_filters:
            filtered_data.append(row)
    return filtered_data