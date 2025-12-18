"""
QUESTION:
Implement a function `correct_data_skew` that takes a list of integers representing data sizes and returns a list of integers representing the sizes of data in each partition after correcting the data skew. The function should ensure that the data is evenly distributed across all partitions.

The function should take two parameters: `data_sizes` and `num_partitions`. `data_sizes` is a list of integers representing the sizes of the data, and `num_partitions` is an integer representing the number of partitions.

The function should return a list of integers, where each integer represents the size of the data in each partition after correcting the data skew.

For example, if the input is `correct_data_skew([100, 200, 50, 300], 3)`, the function should return a list of integers representing the sizes of data in each partition after correcting the data skew.
"""

def correct_data_skew(data_sizes, num_partitions):
    total_size = sum(data_sizes)
    base_size, remainder = divmod(total_size, num_partitions)
    return [base_size + 1] * remainder + [base_size] * (num_partitions - remainder)