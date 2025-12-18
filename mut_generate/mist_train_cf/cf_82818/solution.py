"""
QUESTION:
Implement a function named `maxDistance` that takes four inputs: `target` (the destination in miles), `startFuel` (the initial amount of fuel in liters), `stations` (a list of gas stations where each station is represented as a list `[position, fuel]` with `position` being the miles from the starting position and `fuel` being the liters of gas available), and `maxStops` (the maximum number of refueling stops allowed). The function should return the maximum distance the car can travel. The car uses 1 liter of gas per 1 mile driven, and refueling is possible at gas stations. If the car cannot reach the destination, return the maximum distance it can travel before running out of fuel. The restrictions on the inputs are: `1 <= target, startFuel, stations[i][1] <= 10^9`, `0 <= stations.length <= 500`, `0 < stations[0][0] < stations[1][0] < ... < stations[stations.length-1][0] < target`, and `0 <= maxStops <= stations.length`.
"""

import heapq
def maxDistance(target, startFuel, stations, maxStops):
    pq = []
    stations.append([target, 0])
    res, prev = 0, 0
    for i in range(len(stations)):
        startFuel -= stations[i][0] - prev
        while maxStops >= 0 and startFuel < 0:
            if pq:
                startFuel += -heapq.heappop(pq)
                maxStops -= 1
            else:
                return -1
        if startFuel < 0:
            return -1
        heapq.heappush(pq, -stations[i][1])
        prev = stations[i][0]
    return prev if startFuel >= 0 else -1