"""
QUESTION:
Create a function `generate_histogram` that takes a list of integers as input and returns a list of tuples representing a histogram. The histogram should only include numbers from the input list that are divisible by 3, with their frequency of occurrence. The histogram should be sorted in descending order based on frequency. The function should not print or display any output.
"""

def generate_histogram(numbers):
    histogram = {}
    for num in numbers:
        if num % 3 == 0:
            if num in histogram:
                histogram[num] += 1
            else:
                histogram[num] = 1
    return sorted(histogram.items(), key=lambda x: x[1], reverse=True)