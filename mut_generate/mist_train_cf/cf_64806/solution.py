"""
QUESTION:
Construct a function named `list_processor` that takes three arguments: `list_one` (a list of integers), `multiplier` (an integer), and `power` (an integer). The function should return a new list where each element is the result of raising the corresponding element in `list_one` to the `power`, then multiplying by `multiplier`. If the result exceeds 100, the new list should contain 'Overflow' instead. The function should also handle any errors that may occur during computation.
"""

def list_processor(list_one, multiplier, power):
    try:
        return [i**power*multiplier if i**power*multiplier <= 100 else 'Overflow' for i in list_one]
    except Exception as e:
        print("An error occurred:", e)