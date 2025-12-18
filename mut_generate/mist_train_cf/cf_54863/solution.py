"""
QUESTION:
Create a function named `partition_even_sum` that takes a string of comma-separated numbers as input. The function should partition the input sequence into two distinct segments such that the sum of the numbers in each segment is even. If the total sum of the input sequence is odd, or if it is impossible to partition the sequence into two segments with even sums, the function should return an error message.
"""

def partition_even_sum(input_string):
    numbers = list(map(int, input_string.split(',')))
    total_sum = sum(numbers)
    if total_sum % 2 != 0:
        return "Cannot partition the sequence into two distinct segments with an aggregate value that is even."

    target_sum = total_sum // 2
    current_sum = 0
    partition_point = -1
    for i, num in enumerate(numbers):
        if current_sum == target_sum:
            partition_point = i
            break
        current_sum += num

    if partition_point == -1:
        return "Cannot partition the sequence into two distinct segments with an aggregate value that is even."
    else:
        return ','.join(map(str, numbers[:partition_point])), ','.join(map(str, numbers[partition_point:]))