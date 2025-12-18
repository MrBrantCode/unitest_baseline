"""
QUESTION:
Create a program with three functions: `mean`, `mode`, and `median`. The input to these functions is a list of mixed data types, including integers, floats, and strings. The `mean` function should calculate the average of all numerical values in the list and return the result as a float. The `mode` function should find all elements (numerical or non-numerical) that appear most frequently in the list and return them as a list. The `median` function should calculate the middle value of the numerical values in the sorted list. If the list contains only non-numerical data, the `mean` and `median` functions should return 0 and None respectively. The `mode` function should be able to handle both numerical and non-numerical data.
"""

from collections import Counter
from typing import List, Union

def entrance(lst: List[Union[int, float, str]]) -> tuple:
    def mean() -> float:
        num_lst = [i for i in lst if isinstance(i, (int, float))]
        return sum(num_lst) / len(num_lst) if num_lst else 0

    def mode() -> List[Union[int, float, str]]:
        count_dict = Counter(lst)
        max_val = max(list(count_dict.values()))
        mode_val = [num for num, freq in count_dict.items() if freq == max_val]
        return mode_val

    def median() -> float:
        num_lst = sorted([i for i in lst if isinstance(i, (int, float))])
        length = len(num_lst)
        if length < 1:
            return None
        if length % 2 == 0:
            return (num_lst[(length - 1)//2] + num_lst[(length + 1)//2]) / 2
        else:
            return num_lst[(length - 1)//2]

    return mean(), mode(), median()