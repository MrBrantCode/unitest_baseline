"""
QUESTION:
Implement a function called `load_balancer` that takes two parameters: the total number of incoming requests (`total_requests`) and the number of worker processes (`num_workers`). The function should return a dictionary representing the distribution of requests to each worker process, ensuring that each worker receives as close to an equal number of requests as possible. The function signature should be `def load_balancer(total_requests: int, num_workers: int) -> dict:`.
"""

def load_balancer(total_requests: int, num_workers: int) -> dict:
    requests_per_worker = total_requests // num_workers
    remaining_requests = total_requests % num_workers

    distribution = {}

    for worker in range(1, num_workers + 1):
        if remaining_requests > 0:
            distribution[worker] = requests_per_worker + 1
            remaining_requests -= 1
        else:
            distribution[worker] = requests_per_worker

    return distribution