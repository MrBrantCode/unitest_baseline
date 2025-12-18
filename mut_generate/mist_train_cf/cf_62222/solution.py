"""
QUESTION:
Create a function named `some_func` that takes four parameters: `upper`, `middle`, `lower`, and `column`, where `upper`, `middle`, and `lower` are integers and `column` is a list of integers. The function should return a list of three lists of integers. The function should iterate over the `column` list and append values to the `upper_row`, `middle_row`, and `lower_row` lists based on the current value in `column`. If any of `upper`, `middle`, or `lower` is greater than 0 after iterating over the entire `column` list, the function should return an empty list. Otherwise, the function should return a list containing `upper_row`, `middle_row`, and `lower_row`.
"""

def entance(upper: int, middle: int, lower: int, column: list[int]) -> list[list[int]]:
    upper_row, middle_row, lower_row = [], [], []
    for num in column:
        if num == 2:
            if upper > 0 and lower > 0:
                upper -= 1
                lower -= 1
                upper_row.append(1)
                middle_row.append(0)
                lower_row.append(1)
            else:
                return []
        elif num == 1:
            if upper > 0:
                upper -= 1
                upper_row.append(1)
                middle_row.append(0)
                lower_row.append(0)
            elif middle > 0:
                middle -= 1
                upper_row.append(0)
                middle_row.append(1)
                lower_row.append(0)
            elif lower > 0:
                lower -= 1
                upper_row.append(0)
                middle_row.append(0)
                lower_row.append(1)
            else:
                return []
        else:
            upper_row.append(0)
            middle_row.append(0)
            lower_row.append(0)
    if upper != 0 or middle != 0 or lower != 0:
        return []
    else:
        return [upper_row, middle_row, lower_row]