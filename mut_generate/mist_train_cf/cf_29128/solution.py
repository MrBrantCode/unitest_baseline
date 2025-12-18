"""
QUESTION:
Write a function `optimize_dask_client` that takes two integers as inputs: `system_memory_gb` representing the total memory capacity of the system in gigabytes and `csv_file_size_gb` representing the size of the input CSV file in gigabytes. The function should return a tuple `(n_workers, threads_per_worker, memory_limit)` representing the optimized Dask client configuration, where `n_workers` is the optimal number of workers, `threads_per_worker` is the optimal number of threads per worker, and `memory_limit` is the optimal memory limit for the Dask client in gigabytes. The optimization should aim to utilize the available memory efficiently while ensuring that the processing can be performed in a distributed manner.
"""

import math

def optimize_dask_client(system_memory_gb, csv_file_size_gb):
    # Calculate the optimal number of workers based on the size of the input CSV file and system memory
    n_workers = max(1, math.ceil(csv_file_size_gb / 2))  

    # Calculate the optimal memory limit per worker based on the available system memory and the number of workers
    memory_per_worker_gb = max(1, math.floor(system_memory_gb / n_workers))  

    # Calculate the optimal number of threads per worker based on the workload and system characteristics
    threads_per_worker = 1  

    # Set the memory limit for the Dask client based on the memory per worker and the number of workers
    memory_limit = f"{memory_per_worker_gb}GB"

    return n_workers, threads_per_worker, memory_limit