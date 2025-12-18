"""
QUESTION:
Implement a function `median_and_mode` that calculates the median and mode of a list of integers without sorting the list or using built-in functions. The function should handle lists with an even or odd number of elements, negative numbers, and duplicate values. If all elements appear only once, the mode should be `None`.
"""

def median_and_mode(lst: list):
    """
    Return a tuple with median and mode of elements in the list lst without sorting it or using built-in functions.
    Handles even and odd number of elements, negatives, and duplicates.
    If all elements appear only once, the mode should be `None`.
    """
    def _quickselect(lst: list, k: int):
        if len(lst) == 1:
            return lst[0]

        pivot = lst[len(lst) // 2]

        lows = [percentage for percentage in lst if percentage < pivot]
        highs = [percentage for percentage in lst if percentage > pivot]
        pivots = [percentage for percentage in lst if percentage == pivot]

        if k < len(lows):
            return _quickselect(lows, k)
        elif k < len(lows) + len(pivots):
            return pivots[0]
        else:
            return _quickselect(highs, k - len(lows) - len(pivots))

    lst_length = len(lst)
    if lst_length % 2 == 1:
        median = _quickselect(lst, lst_length // 2)
    else:
        median = (_quickselect(lst, lst_length // 2) +
                  _quickselect(lst, lst_length // 2 - 1)) / 2

    count = {}
    highest_count = 0
    mode = None
    for num in lst:
        count[num] = count.get(num, 0) + 1
        if count[num] > highest_count:
            highest_count = count[num]
            mode = num

    if highest_count == 1:
        mode = None

    return median, mode