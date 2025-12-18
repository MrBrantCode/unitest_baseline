"""
QUESTION:
Implement a function round_robin_scheduling that takes in two parameters: processes (a list of integers representing the burst times of processes) and time_slice (an integer representing the time slice for each process). The function should return the total time to schedule all processes using the round-robin scheduling algorithm. Assume that the processes are listed in the order they arrive and the time slice is a fixed, non-zero value.
"""

def round_robin_scheduling(processes, time_slice):
    """
    This function implements the round-robin scheduling algorithm.
    
    Parameters:
    processes (list): A list of integers representing the burst times of processes.
    time_slice (int): An integer representing the time slice for each process.
    
    Returns:
    int: The total time to schedule all processes.
    """
    remaining_burst = processes[:]  # Create a copy of the processes list
    time = 0

    while True:
        done = True
        
        for i in range(len(processes)):
            if remaining_burst[i] > 0:
                done = False
                
                if remaining_burst[i] > time_slice:
                    time += time_slice
                    remaining_burst[i] -= time_slice
                else:
                    time += remaining_burst[i]
                    remaining_burst[i] = 0

        if done:
            break

    return time