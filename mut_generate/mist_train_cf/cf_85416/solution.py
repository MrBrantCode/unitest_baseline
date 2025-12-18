"""
QUESTION:
You are given an array `tasks` where `tasks[i] = [actuali, minimumi]` with `1 <= actuali <= minimumi <= 10^4`. Return the minimum initial amount of energy you will need to finish all the tasks. The energy spent to finish a task is the actual amount of energy for that task, and you can finish the tasks in any order. 

Note that the tasks are finished with the given energy, and there is no energy recovery after each task.
"""

import heapq

def entrance(tasks):
    tasks.sort(key=lambda x:(x[1]-x[0], -x[1]))
    res = cur = sum(a for a, m in tasks)
    for a, m in tasks:
        cur -= a
        if cur < m:
            res += m - cur
            cur = m
    return res