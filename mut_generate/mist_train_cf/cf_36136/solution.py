"""
QUESTION:
Implement a function `allocate_resources` that allocates virtual machine instances to incoming requests based on their resource requirements and the available capacity of the platform. The function takes four inputs: `total_cpu`, `total_memory`, `total_storage`, and `requests`. The `total_cpu`, `total_memory`, and `total_storage` are integers representing the total available CPU, memory, and storage capacity on the platform. The `requests` is a list of tuples, where each tuple contains three integers representing the CPU, memory, and storage requirements of a request. The function should return a list of booleans indicating whether each request can be successfully allocated based on the available resources in a first-come, first-served manner.
"""

def allocate_resources(total_cpu, total_memory, total_storage, requests):
    available_cpu = total_cpu
    available_memory = total_memory
    available_storage = total_storage
    allocation_status = []

    for request in requests:
        cpu_req, memory_req, storage_req = request
        if cpu_req <= available_cpu and memory_req <= available_memory and storage_req <= available_storage:
            available_cpu -= cpu_req
            available_memory -= memory_req
            available_storage -= storage_req
            allocation_status.append(True)
        else:
            allocation_status.append(False)

    return allocation_status