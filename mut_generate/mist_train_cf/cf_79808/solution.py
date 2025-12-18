"""
QUESTION:
Write a function called `num_trips` that takes two parameters, `total_rocks` and `rocks_per_trip`, where `total_rocks` is the total number of rocks to be transferred and `rocks_per_trip` is the maximum number of rocks that can be carried at once. The function should return the minimum number of trips required to transfer all the rocks.
"""

def num_trips(total_rocks, rocks_per_trip):
    return -(-total_rocks // rocks_per_trip)