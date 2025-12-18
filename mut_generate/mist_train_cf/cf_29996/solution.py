"""
QUESTION:
Write a function `process_lists(cost_list, SEM_list)` that takes two lists as input and returns five lists. It should extract elements from `SEM_list` at indices [0, 12) with a step of 2, store them in `tRRT_SEM_list`. Then it should extract elements from `cost_list` and `SEM_list` at indices [12, 24) with a step of 4, store them in `biRRT_cost_list` and `biRRT_SEM_list` respectively. Finally, it should extract elements from `cost_list` and `SEM_list` at indices [14, 24) with a step of 4, store them in `tbiRRT_cost_list` and `tbiRRT_SEM_list` respectively. The input lists will have at least 24 elements each.
"""

def process_lists(cost_list, SEM_list):
    tRRT_SEM_list = SEM_list[0:12:2]
    biRRT_cost_list = cost_list[12:24:4]
    biRRT_SEM_list = SEM_list[12:24:4]
    tbiRRT_cost_list = cost_list[14:24:4]
    tbiRRT_SEM_list = SEM_list[14:24:4]
    return tRRT_SEM_list, biRRT_cost_list, biRRT_SEM_list, tbiRRT_cost_list, tbiRRT_SEM_list