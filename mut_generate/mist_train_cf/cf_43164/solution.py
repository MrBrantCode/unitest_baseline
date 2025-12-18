"""
QUESTION:
Create a function `calculate_performance_metrics` that takes a dictionary `metrics` as input, containing keys 'scylla_reactor_aio_bytes_read', 'scylla_reactor_aio_bytes_write', 'scylla_reactor_aio_errors', 'scylla_reactor_aio_reads', and 'scylla_reactor_aio_writes'. The function should return a dictionary with the following calculated metrics: 'average_bytes_read_per_operation', 'average_bytes_write_per_operation', and 'error_rate'. The 'average_bytes_read_per_operation' is calculated as 'scylla_reactor_aio_bytes_read' divided by 'scylla_reactor_aio_reads', 'average_bytes_write_per_operation' is 'scylla_reactor_aio_bytes_write' divided by 'scylla_reactor_aio_writes', and 'error_rate' is 'scylla_reactor_aio_errors' divided by the sum of 'scylla_reactor_aio_reads' and 'scylla_reactor_aio_writes'. The function should handle division by zero and return the calculated metrics rounded to two decimal places.
"""

def calculate_performance_metrics(metrics):
    reads = metrics['scylla_reactor_aio_reads']
    writes = metrics['scylla_reactor_aio_writes']

    if reads == 0 and writes == 0:
        return {
            'average_bytes_read_per_operation': 0.00,
            'average_bytes_write_per_operation': 0.00,
            'error_rate': 0.00
        }
    elif reads == 0:
        return {
            'average_bytes_read_per_operation': 0.00,
            'average_bytes_write_per_operation': round(metrics['scylla_reactor_aio_bytes_write'] / writes, 2),
            'error_rate': round(metrics['scylla_reactor_aio_errors'] / (reads + writes), 2)
        }
    elif writes == 0:
        return {
            'average_bytes_read_per_operation': round(metrics['scylla_reactor_aio_bytes_read'] / reads, 2),
            'average_bytes_write_per_operation': 0.00,
            'error_rate': round(metrics['scylla_reactor_aio_errors'] / (reads + writes), 2)
        }
    else:
        return {
            'average_bytes_read_per_operation': round(metrics['scylla_reactor_aio_bytes_read'] / reads, 2),
            'average_bytes_write_per_operation': round(metrics['scylla_reactor_aio_bytes_write'] / writes, 2),
            'error_rate': round(metrics['scylla_reactor_aio_errors'] / (reads + writes), 2)
        }