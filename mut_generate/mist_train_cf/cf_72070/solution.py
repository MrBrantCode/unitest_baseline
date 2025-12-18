"""
QUESTION:
Given an integer array `jobs` where `jobs[i]` is the amount of time it takes to complete the `ith` job, an integer array `priority` where `priority[i]` is the priority of the `ith` job, and an integer `k` representing the number of workers, devise an optimal assignment such that the maximum working time of any worker is minimized, while also ensuring that jobs with higher priority are assigned first.

Return the minimum possible maximum working time of any assignment.

Constraints: `1 <= k <= jobs.length <= 12` and `1 <= jobs[i], priority[i] <= 10^7`
"""

import heapq

def entrance(jobs, priority, k):
    # Combine jobs and priority into a list of tuples and sort in in reverse order (highest priority first)
    priority_jobs = sorted([(p, j) for j, p in zip(jobs, priority)], reverse=True)

    # Initialize a min heap for the workers
    workers = [0]*k
    heapq.heapify(workers)

    maxTime = 0
    # Assign each job to a worker
    for p, j in priority_jobs:
        # Get the worker which has done the least work so far
        workerTime = heapq.heappop(workers)
        # Update the worker's total working time
        workerTime += j
        # Push the updated worker's working time back into the heap
        heapq.heappush(workers, workerTime)
        # Update the maximum working time
        maxTime = max(maxTime, workerTime)

    return maxTime