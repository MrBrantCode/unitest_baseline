"""
QUESTION:
Write a function `select_tasks(max_flops, max_epochs, select_num, tasks)` that takes in the maximum FLOPS `max_flops`, maximum epochs `max_epochs`, the number of tasks to select `select_num`, and a list of tasks `tasks`. Each task in `tasks` is a dictionary containing the keys `flops` and `epochs`. The function should return a list of indices of the selected tasks such that the total FLOPS is maximized while ensuring that the total number of epochs does not exceed `max_epochs`. The selected tasks must be a subset of `select_num` tasks from `tasks`.
"""

from typing import List

def entrance(max_flops, max_epochs, select_num, tasks) -> List[int]:
    dp = [[[0, []] for _ in range(max_epochs + 1)] for _ in range(len(tasks) + 1)]
    
    for i in range(1, len(tasks) + 1):
        for j in range(1, max_epochs + 1):
            if tasks[i - 1]['epochs'] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                prev_max_flops, _ = dp[i - 1][j]
                curr_max_flops = dp[i - 1][j - tasks[i - 1]['epochs']][0] + tasks[i - 1]['flops']
                if curr_max_flops > prev_max_flops:
                    dp[i][j] = [curr_max_flops, dp[i - 1][j - tasks[i - 1]['epochs']][1] + [i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
                    
    max_flops = 0
    selected_tasks = []
    for i in range(max_epochs, -1, -1):
        if dp[-1][i][0] > max_flops and len(dp[-1][i][1]) <= select_num:
            max_flops = dp[-1][i][0]
            selected_tasks = dp[-1][i][1]
            
    return selected_tasks