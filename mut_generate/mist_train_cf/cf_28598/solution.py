"""
QUESTION:
Implement the function `minimize_waiting_time(jobs)` that takes a list of jobs, where each job is a tuple `(start_time, duration)`, and returns the order in which the jobs should be executed to minimize the total waiting time. The total waiting time for a job is the sum of the durations of all jobs that are scheduled to start before it. The input list `jobs` is not guaranteed to be sorted.
"""

def entrance(jobs):
    sorted_jobs = sorted(jobs, key=lambda x: x[1])  # Sort jobs by duration
    return sorted_jobs