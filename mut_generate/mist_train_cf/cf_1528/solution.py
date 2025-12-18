"""
QUESTION:
Write a function named `create_histogram` that takes a list of numbers as input and returns a histogram where the keys are unique pairs of numbers from the list and the values are the counts of each pair. The function should have a time complexity of O(n^2) (not O(n^3)) and a space complexity of O(n^2) (not O(1)).
"""

def create_histogram(numbers):
    histogram = {}
    
    # Iterate through each pair of numbers in the list
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            pair = (numbers[i], numbers[j])
            
            # Count the occurrence of each unique pair
            if pair in histogram:
                histogram[pair] += 1
            else:
                histogram[pair] = 1
    
    return histogram