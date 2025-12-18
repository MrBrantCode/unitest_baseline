"""
QUESTION:
Create a function `calculate_fruit_weight` that takes a list of fruit objects as input, where each fruit object has a `kind` attribute (e.g., 'Pears', 'Apples', 'Oranges') and a `weights` attribute (a list of integer weights for each subtype of fruit). The function must also take a `total_fruit_weight` parameter representing the total weight of fruits required.

The function should return the quantities of each subtype of fruit required to make up the total weight, subject to the following constraints:

- The total weight of pears must be at least 5kg.
- The total weight of apples must not exceed 20kg.
- There must be an equal amount of each kind of oranges.
- All quantities must be integers (no half or partial quantities of any fruit type).

The function should be designed to be easily modified for different requirements and fruit types in the future.
"""

def calculate_fruit_weight(fruit_list, total_fruit_weight):
    min_p = 5
    max_a = 20

    for f in fruit_list:
        if f.get_kind() == 'Pears':
            for w in f.get_weights():
                if min_p / w == int(min_p / w):
                    min_p_qty = min_p / w
                    total_fruit_weight -= min_p
        elif f.get_kind() == 'Apples':
            for w in f.get_weights():
                if max_a / w == int(max_a / w):
                    max_a_qty = max_a / w
                    total_fruit_weight -= max_a
        elif f.get_kind() == 'Oranges':
            for w in f.get_weights():
                o_qty = total_fruit_weight / (w * 3)
                
    return min_p_qty, max_a_qty, o_qty