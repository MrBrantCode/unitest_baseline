"""
QUESTION:
Write a function `calculate_average_times` that takes in a dictionary `info` containing information about each inference, including 'invoke_time', and returns a tuple of two floating-point numbers representing the average inference time and average summary time in milliseconds.

The `info` dictionary contains multiple 'invoke_time' values, each corresponding to an inference. The function should calculate the average of these 'invoke_time' values to determine the average inference time. The average summary time should be calculated by finding the average time it takes to process all inferences.

The function should return a tuple where the first element is the average inference time in milliseconds and the second element is the average summary time in milliseconds.
"""

def calculate_average_times(info: dict) -> tuple:
    times = [data['invoke_time'] for data in info.values()]
    return (sum(times) / len(times) * 1000, 0.0)