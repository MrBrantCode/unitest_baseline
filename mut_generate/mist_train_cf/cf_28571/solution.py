"""
QUESTION:
Implement a function `assignTask(cpuLists, taskId, taskDuration)` that assigns a new task to the CPU core with the least total task duration. The function should return the index of the CPU core to which the task was assigned.

The function takes in three parameters: 
- `cpuLists`: A dictionary representing the CPU cores and their assigned tasks, where each key represents a CPU core and its associated value is a dictionary containing the list of tasks assigned to that core.
- `taskId`: The unique identifier for the new task to be assigned.
- `taskDuration`: The time required to complete the new task.

If multiple cores have the same total task duration, the task should be assigned to the core with the lowest index.
"""

def assignTask(cpuLists, taskId, taskDuration):
    min_total_duration = float('inf')
    min_index = None

    for index, core in cpuLists.items():
        total_duration = sum(task["taskDuration"] for task in core["tasks"])
        if total_duration < min_total_duration or (total_duration == min_total_duration and int(index) < int(min_index)):
            min_total_duration = total_duration
            min_index = index

    cpuLists[min_index]["tasks"].append({"taskId": taskId, "taskDuration": taskDuration})
    return int(min_index)