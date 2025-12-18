"""
QUESTION:
Write a function `numOfMinutes(n, headID, manager, informTime, channel)` that takes five parameters: `n` representing the number of employees, `headID` representing the ID of the head of the company, `manager` representing an array of the direct manager of each employee, `informTime` representing the time each employee needs to inform their direct subordinates, and `channel` representing the communication channel each employee uses. The function should return the number of minutes needed to inform all employees about an urgent news. The company has a tree structure, the head of the company is the only employee with `headID`, and the `i-th` employee needs `informTime[i]` minutes to inform all of his direct subordinates multiplied by the `channel[i]` factor. Constraints: `1 <= n <= 10^5`, `0 <= headID < n`, `manager.length == n`, `0 <= manager[i] < n`, `manager[headID] == -1`, `informTime.length == n`, `0 <= informTime[i] <= 1000`, `channel.length == n`, and `1 <= channel[i] <= 10`.
"""

from collections import defaultdict

def numOfMinutes(n, headID, manager, informTime, channel):
    subor = defaultdict(list)
    for i, m in enumerate(manager):
        subor[m].append(i)

    def dfs(i):
        times = [dfs(j) for j in subor[i]]
        return max(times, default=0) + informTime[i]*channel[i]

    return dfs(headID)