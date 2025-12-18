"""
QUESTION:
Write a function `getImportance(employees, id, level)` that calculates the total importance value of an employee with the given `id` and all their subordinates up to the given `hierarchical level`. The function takes a list of `Employee` objects, each containing `id`, `importance`, `level`, and `subordinates`, as input and returns an integer representing the total importance value. Assume the maximum number of employees won't exceed 2000 and the maximum hierarchical level won't exceed the number of employees.
"""

class Employee:
    def __init__(self, id: int, importance: int, level: int, subordinates: list):
        self.id = id
        self.importance = importance
        self.level = level
        self.subordinates = subordinates

def getImportance(employees: list, id: int, level: int) -> int:
    emap = {e.id: e for e in employees}

    def dfs(eid, level_limit):
        if emap[eid].level > level_limit:
            return 0
        return emap[eid].importance + sum(dfs(sid, level_limit - 1) for sid in emap[eid].subordinates)

    return dfs(id, level)