"""
QUESTION:
Write a function `calculate_average_completion_time` that calculates the lowest possible average completion time for a list of tasks with given service times. The function should take a list of integers representing the service times of tasks as input and return the lowest possible average completion time. The tasks are executed on a single processor and the goal is to minimize the average completion time using the Shortest Job First (SJF) or Shortest Remaining Time First (SRTF) scheduling algorithm.
"""

def calculate_average_completion_time(service_times):
    """
    This function calculates the lowest possible average completion time 
    for a list of tasks with given service times using the SJF or SRTF algorithm.

    Args:
    service_times (list): A list of integers representing the service times of tasks.

    Returns:
    float: The lowest possible average completion time.
    """
    # The jobs would be queued in increasing order of service time if SJF or SRTF is being used
    service_times.sort()

    completion_times = []
    previous_time = 0

    # Each job's completion time is the sum of its own service time and the service times of all previous jobs
    for current_time in service_times:
        total_time = previous_time + current_time
        completion_times.append(total_time)
        previous_time = total_time

    # Average completion time is the sum of all completion times divided by the number of jobs
    average_completion_time = sum(completion_times) / len(completion_times)

    return average_completion_time