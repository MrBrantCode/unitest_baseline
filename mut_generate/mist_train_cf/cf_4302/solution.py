"""
QUESTION:
Design a function named `optimize_parallel_processing` with the following restrictions:
 
This function should take in a list of tasks and the number of threads as input parameters. It should return a list of tasks assigned to each thread and the total execution time. Assume tasks are independent and the execution time of each task is given. The goal is to minimize the total execution time by distributing tasks optimally among threads.

Note: The function does not require any specific implementation of multithreading or parallel processing. It only needs to provide a theoretical distribution of tasks among threads to minimize the total execution time.
"""

def optimize_parallel_processing(tasks, num_threads):
    """
    This function distributes tasks among threads to minimize total execution time.

    Args:
        tasks (list): A list of tasks with their execution times.
        num_threads (int): The number of threads.

    Returns:
        list: A list of tasks assigned to each thread and the total execution time.
    """
    tasks.sort(reverse=True)  # Sort tasks in descending order of their execution times
    thread_tasks = [[] for _ in range(num_threads)]  # Initialize threads with no tasks
    thread_times = [0] * num_threads  # Initialize thread times to 0

    for task in tasks:
        # Assign the task to the thread with the minimum current execution time
        min_time_thread = thread_times.index(min(thread_times))
        thread_tasks[min_time_thread].append(task)
        thread_times[min_time_thread] += task

    return thread_tasks, max(thread_times)

# Example usage (commented out):
# tasks = [10, 5, 8, 3, 2, 1]
# num_threads = 3
# assigned_tasks, total_time = optimize_parallel_processing(tasks, num_threads)
# print("Assigned tasks:", assigned_tasks)
# print("Total execution time:", total_time)