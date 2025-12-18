"""
QUESTION:
Create a function called `create_histogram` that takes a list of numbers as input and returns a dictionary where the keys are unique pairs of numbers from the list and the values are the counts of each pair. The function should have a time complexity of less than or equal to O(n^2), not O(n^3), because it only needs two nested loops to compare each pair of numbers, and a space complexity of O(n) or less because the number of unique pairs is less than or equal to n*(n-1)/2.
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