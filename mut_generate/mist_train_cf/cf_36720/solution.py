"""
QUESTION:
Implement a function named `round_robin_scheduling` that takes two parameters: `time_quantum` and `processes`. The `time_quantum` is a fixed time allocated to each process, and `processes` is a list of dictionaries where each dictionary represents a process with keys "pid", "arrival_time", "burst_time", and "priority". The function should simulate a round-robin scheduling algorithm, returning a list of process IDs in the order they are executed. The algorithm should allocate the given time quantum to each process, placing any incomplete process at the end of the queue to wait for its next turn. Assume the input processes are sorted by their arrival time.
"""

def round_robin_scheduling(time_quantum, processes):
    queue = processes.copy()
    execution_order = []
    current_time = 0
    while queue:
        process = queue.pop(0)
        if process["burst_time"] > time_quantum:
            execution_order.append(process["pid"])
            current_time += time_quantum
            process["burst_time"] -= time_quantum
            queue.append(process)
        else:
            execution_order.append(process["pid"])
            current_time += process["burst_time"]
            process["burst_time"] = 0
    return execution_order