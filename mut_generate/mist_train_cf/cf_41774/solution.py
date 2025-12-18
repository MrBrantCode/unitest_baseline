"""
QUESTION:
Implement a function `calculate_total_bytes_read` that takes a file object `file_obj` and an integer `chunk_size` as input, reads the file in chunks of `chunk_size` bytes, and returns the total number of bytes read from the file. The function should continue reading the file until the end is reached, at which point it returns the total number of bytes read.
"""

def calculate_total_bytes_read(file_obj, chunk_size):
    total_bytes_read = 0
    while True:
        data = file_obj.read(chunk_size)
        read_size = len(data)
        if not read_size:
            break
        total_bytes_read += read_size
    return total_bytes_read