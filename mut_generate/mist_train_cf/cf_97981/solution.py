"""
QUESTION:
Modify the `round_robin` function to track the total time taken for all processes to complete in the Round Robin scheduling algorithm. The function should take a list of processes and a time slice as input, and return the total time taken for all processes to complete.
"""

# function to implement Round Robin scheduling algorithm
def round_robin(process_list, time_slice):
    queue = process_list.copy()
    total_time = 0
    while queue:
        process = queue.pop(0)
        if process["remaining_time"] <= time_slice:
            total_time += process["remaining_time"]
        else:
            total_time += time_slice
            process["remaining_time"] -= time_slice
            queue.append(process)
    return total_time