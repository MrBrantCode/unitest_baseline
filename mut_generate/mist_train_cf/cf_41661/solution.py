"""
QUESTION:
Calculate the optimal chunk size for processing log files in a distributed environment. The function `calculate_optimal_chunk_size` takes two inputs: `total_size` (the total size of the log files) and `cloud_size` (the number of nodes in the cloud). The function should return the optimal chunk size based on the following constraints:
- The default log base 2 chunk size is 22.
- Each node should process a local parse size of at least `total_size / cloud_size`.
- There must be at least 10 rows (lines) per chunk.
- The total number of chunk POJOs per node should not exceed 2 million.
"""

def calculate_optimal_chunk_size(total_size, cloud_size, max_line_length):
    default_log2_chunk_size = 20+2
    default_chunk_size = 1 << default_log2_chunk_size
    local_parse_size = int(total_size / cloud_size)
    min_number_rows = 10  
    per_node_chunk_count_limit = 1 << 21  

    optimal_chunk_size = max(default_chunk_size, local_parse_size)
    if optimal_chunk_size / max_line_length < min_number_rows:
        optimal_chunk_size = min_number_rows * max_line_length
    if total_size / optimal_chunk_size > per_node_chunk_count_limit:
        optimal_chunk_size = total_size / per_node_chunk_count_limit

    return optimal_chunk_size