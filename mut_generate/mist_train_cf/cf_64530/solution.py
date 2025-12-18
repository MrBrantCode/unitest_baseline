"""
QUESTION:
Write a function named `distance_between_stops` that takes four parameters: `distance`, `start`, `destination`, and `traffic`, and returns the shortest distance between the given `start` and `destination` stops, considering the traffic jams. The `distance` list contains the distances between all pairs of neighboring stops, the `start` and `destination` are the given stops, and the `traffic` list indicates whether there is a traffic jam at each stop. The bus goes along both directions, but cannot stop at stops with traffic jams. The function should work under the following constraints: `1 <= n <= 10^4`, `distance.length == n`, `traffic.length == n`, `0 <= start, destination < n`, and `0 <= distance[i] <= 10^4`.
"""

def distance_between_stops(distance, start, destination, traffic):
    if start > destination:
        start, destination = destination, start
    total = sum(distance)
    clockwise = sum(distance[i] for i in range(start, destination) if not traffic[i])
    counter_clockwise = total - clockwise
    return min(clockwise, counter_clockwise)