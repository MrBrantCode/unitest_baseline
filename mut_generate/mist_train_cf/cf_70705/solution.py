"""
QUESTION:
Write a function `calculate_fertilizer` that determines the quantity of 5lb and 7lb fertilizer bags needed to achieve a target nitrogen content. The function should take an integer target weight as input and return the number of 5lb and 7lb bags required, considering that the number of bags must be integers.
"""

def calculate_fertilizer(target_weight):
    for x in range(target_weight // 5 + 1):
        y = (target_weight - 5 * x) / 7
        if y == int(y) and y >= 0:
            return x, int(y)
    return None