"""
QUESTION:
Given a company with n employees, write a function `numOfMinutes` to calculate the time needed for all employees to be informed if the head employee informs all employees.

The function takes in four parameters: the number of employees n, the ID of the head employee headID, a list of direct managers for each employee, and a list of times it takes for each employee to inform all their subordinates. The function should return the total time needed for all employees to be informed.

The function signature is:
```python
def numOfMinutes(n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
```
"""

from typing import List

def numOfMinutes(n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
    children = [[] for i in range(n)]
    for i, m in enumerate(manager):
        if m >= 0:
            children[m].append(i)

    def dfs(value):
        if not children[value]:
            return 0
        max_time = 0
        for child in children[value]:
            max_time = max(max_time, dfs(child))
        return informTime[value] + max_time

    return dfs(headID)