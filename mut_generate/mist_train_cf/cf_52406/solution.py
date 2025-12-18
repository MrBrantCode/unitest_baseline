"""
QUESTION:
Design a function `optimize_travel_cost` that takes as input a 3D array `costs` where `costs[i][j][k]` is the cost of visiting city `j` at time `k` after visiting city `i`, a list `mandatory_cities` of cities that must be visited, a maximum budget `max_budget`, and the number of cities `n`. The function should return the minimum total cost of visiting all cities in `mandatory_cities` without exceeding `max_budget`.
"""

import heapq

def optimize_travel_cost(costs, mandatory_cities, max_budget, n):
    def dijkstra(current_city, current_cost, visited):
        queue = [(current_cost, current_city, visited)]
        min_cost = float('inf')
        while queue:
            cost, city, visited_cities = heapq.heappop(queue)
            if cost > min_cost:
                break
            if all(city in visited_cities for city in mandatory_cities):
                min_cost = min(min_cost, cost)
            for next_city in range(n):
                if next_city not in visited_cities:
                    for time_slot in range(len(costs[city][next_city])):
                        new_cost = cost + costs[city][next_city][time_slot]
                        if new_cost <= max_budget:
                            new_visited = visited_cities | {next_city}
                            heapq.heappush(queue, (new_cost, next_city, new_visited))
        return min_cost

    min_cost = float('inf')
    for start_city in range(n):
        min_cost = min(min_cost, dijkstra(start_city, 0, {start_city}))
    return min_cost if min_cost != float('inf') else -1