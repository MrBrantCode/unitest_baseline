"""
QUESTION:
We have a list of bus routes. Each routes[i] is a bus route that the i-th bus repeats forever. For example if routes[0] = [1, 5, 7], this means that the first bus (0-th indexed) travels in the sequence 1->5->7->1->5->7->1->... forever.
We start at bus stop S (initially not on a bus), and we want to go to bus stop T. Travelling by buses only, what is the least number of buses we must take to reach our destination? Return -1 if it is not possible.
Example:
Input: 
routes = [[1, 2, 7], [3, 6, 7]]
S = 1
T = 6
Output: 2
Explanation: 
The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.

 
Constraints:

1 <= routes.length <= 500.
1 <= routes[i].length <= 10^5.
0 <= routes[i][j] < 10 ^ 6.
"""

from collections import defaultdict
from typing import List

def min_buses_to_destination(routes: List[List[int]], start: int, target: int) -> int:
    if start == target:
        return 0
    
    max_int = 10 ** 6
    start_routes = set()
    end_routes = set()
    route_connections = defaultdict(set)
    sequence_to_route_id_dict = {}
    route_to_minbuscount = defaultdict(lambda: max_int)
    
    for r_id, r in enumerate(routes):
        for s in r:
            if s == start:
                start_routes.add(r_id)
                route_to_minbuscount[r_id] = 1
            if s == target:
                end_routes.add(r_id)
            if s in sequence_to_route_id_dict:
                route_connections[r_id].add(sequence_to_route_id_dict[s])
                route_connections[sequence_to_route_id_dict[s]].add(r_id)
            sequence_to_route_id_dict[s] = r_id
    
    current_route_buscount = [(s, 1) for s in start_routes]
    
    for r_id, buscount in current_route_buscount:
        for connection in route_connections[r_id]:
            if route_to_minbuscount[connection] > buscount + 1:
                route_to_minbuscount[connection] = buscount + 1
                current_route_buscount.append((connection, buscount + 1))
    
    result = min((route_to_minbuscount[x] for x in end_routes), default=max_int)
    
    return -1 if result == max_int else result