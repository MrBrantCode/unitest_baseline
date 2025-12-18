"""
QUESTION:
Create a function called `killProcesses(pid, ppid, priority, kill)` that takes four parameters: `pid`, `ppid`, `priority`, and `kill`. The function should return a list of process IDs that will be killed when the process with ID `kill` is killed. The process with ID `kill` has a priority restriction that it can only be killed if its priority is less than or equal to the priority of the process that is being killed. The function should return an empty list if the process cannot be killed due to priority restrictions.

The input parameters are: 
- `pid`: a list of process IDs
- `ppid`: a list of parent process IDs corresponding to the processes in `pid`
- `priority`: a list of priorities corresponding to the processes in `pid`
- `kill`: the ID of the process to be killed

Constraints: 
- `n == pid.length`
- `n == ppid.length`
- `n == priority.length`
- `1 <= n <= 5 * 10^4`
- `1 <= pid[i] <= 5 * 10^4`
- `0 <= ppid[i] <= 5 * 10^4`
- `1 <= priority[i] <= 5 * 10^4`
- Only one process has no parent
- All the values of `pid` are unique
- `kill` is guaranteed to be in `pid`
"""

from collections import defaultdict

def killProcesses(pid, ppid, priority, kill):
    graph = defaultdict(list)
    processPriority = {}
    
    for i in range(len(ppid)):
        graph[ppid[i]].append(pid[i])
        processPriority[pid[i]] = priority[i]
    
    killList = []
    stack = [kill]
    
    while stack:
        process = stack.pop()
        
        if processPriority[process] <= processPriority[kill]:
            killList.append(process)
            stack.extend(graph[process])
    
    return killList