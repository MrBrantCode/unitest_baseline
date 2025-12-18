"""
QUESTION:
Create a function to calculate the rolling average of the last 'n' data points. The function should be able to efficiently handle a large number of data points and maintain accuracy even after older data points are dropped.
"""

from collections import deque

def rolling_average(n):
    data = deque(maxlen=n)
    
    def add(value):
        data.append(value)
        
    def average():
        return sum(data) / len(data) if data else 0
    
    return add, average

# Initialize the rolling average with a size of n
n = 10
add, average = rolling_average(n)

# To use the rolling average, add data points using the add function
# and calculate the average using the average function
# Example usage:
# add(1)
# add(2)
# add(3)
# print(average())