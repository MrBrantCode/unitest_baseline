"""
QUESTION:
Given a vehicle with a certain capacity and fuel, determine if it is possible to complete all trips without running out of fuel or exceeding the vehicle's capacity. 

The function `carPooling(trips, capacity, fuel)` should take as input a list of trips where each trip is a list `[num_passengers, start_location, end_location, fuel_consumption]`, the capacity of the vehicle, and the initial fuel in the vehicle. 

The function should return `True` if it is possible to complete all trips and `False` otherwise.

Constraints:
- `trips.length <= 1000`
- `trips[i].length == 4`
- `1 <= trips[i][0] <= 100`
- `0 <= trips[i][1] < trips[i][2] <= 1000`
- `1 <= trips[i][3] <= 10`
- `1 <= capacity <= 100000`
- `1 <= fuel <= 1000000`
"""

import heapq

def entrance(trips, capacity, fuel):
    trips = sorted(trips, key=lambda trip: trip[1]) 
    heap = []
    for num_passengers, start, end, fc in trips:
        fuel -= fc * (end - start) 
        heapq.heappush(heap, -num_passengers)
        while heap and fuel < 0:
            fuel += -heapq.heappop(heap)
        if fuel < 0:
            return False
    return True