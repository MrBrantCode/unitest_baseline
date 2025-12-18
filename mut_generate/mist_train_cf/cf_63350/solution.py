"""
QUESTION:
Create a function `ternary_to_decision_table` that takes a variable `y` and converts the given ternary operator-based comparison conditions for `y` into a matching decision table structure. The function should return the decision table as a list of dictionaries or a 2D list, where each inner list or dictionary represents a row in the table with conditions and the corresponding action. The conditions and actions should be based on the comparison conditions for `y`.
"""

def ternary_to_decision_table(y):
    """
    Convert ternary operator-based comparison conditions for `y` into a matching decision table structure.
    
    Parameters:
    y (int): The variable used in the comparison conditions.
    
    Returns:
    list: A list of dictionaries representing the decision table.
    """

    # Define the conditions and corresponding actions based on the comparison conditions for `y`.
    decision_table = [
        {"condition1": y < 5, "condition2": None, "action": "set result to 'a'"},
        {"condition1": y >= 5, "condition2": y < 10, "action": "set result to 'b'"},
        {"condition1": y >= 10, "condition2": None, "action": "set result to 'c'"},
    ]

    return decision_table