"""
QUESTION:
Design a function `schedule_workload` that assigns workloads over manageable working windows with rest periods in between. The function should take as input an integer `workload`, the minimum and maximum limits for each allocated workload (`min_work`, `max_work`), and the minimum and maximum limits for the duration of the rest periods (`min_rest`, `max_rest`). The function should return a list of tuples, where each tuple contains the allocated workload and the duration of the rest period that follows.
"""

def schedule_workload(workload, min_work, max_work, min_rest, max_rest):
    """
    Assigns workloads over manageable working windows with rest periods in between.

    Args:
        workload (int): The total workload to be allocated.
        min_work (int): The minimum limit for each allocated workload.
        max_work (int): The maximum limit for each allocated workload.
        min_rest (int): The minimum limit for the duration of the rest periods.
        max_rest (int): The maximum limit for the duration of the rest periods.

    Returns:
        list[tuple[int, int]]: A list of tuples, where each tuple contains the allocated workload and the duration of the rest period that follows.
    """

    allocated_workloads = []
    while workload > 0:
        # Calculate the workload for the current window
        current_work = min(max_work, workload)
        current_work = max(min_work, current_work)

        # Calculate the rest period after the current workload
        rest_period = min(max_rest, max_rest - min_rest) + min_rest

        # Add the allocated workload and rest period to the result
        allocated_workloads.append((current_work, rest_period))

        # Update the remaining workload
        workload -= current_work

    return allocated_workloads