"""
QUESTION:
Andrewid the Android is a galaxy-famous detective. He is now chasing a criminal hiding on the planet Oxa-5, the planet almost fully covered with water.

The only dry land there is an archipelago of n narrow islands located in a row. For more comfort let's represent them as non-intersecting segments on a straight line: island i has coordinates [l_{i}, r_{i}], besides, r_{i} < l_{i} + 1 for 1 ≤ i ≤ n - 1.

To reach the goal, Andrewid needs to place a bridge between each pair of adjacent islands. A bridge of length a can be placed between the i-th and the (i + 1)-th islads, if there are such coordinates of x and y, that l_{i} ≤ x ≤ r_{i}, l_{i} + 1 ≤ y ≤ r_{i} + 1 and y - x = a. 

The detective was supplied with m bridges, each bridge can be used at most once. Help him determine whether the bridges he got are enough to connect each pair of adjacent islands.


-----Input-----

The first line contains integers n (2 ≤ n ≤ 2·10^5) and m (1 ≤ m ≤ 2·10^5) — the number of islands and bridges.

Next n lines each contain two integers l_{i} and r_{i} (1 ≤ l_{i} ≤ r_{i} ≤ 10^18) — the coordinates of the island endpoints.

The last line contains m integer numbers a_1, a_2, ..., a_{m} (1 ≤ a_{i} ≤ 10^18) — the lengths of the bridges that Andrewid got.


-----Output-----

If it is impossible to place a bridge between each pair of adjacent islands in the required manner, print on a single line "No" (without the quotes), otherwise print in the first line "Yes" (without the quotes), and in the second line print n - 1 numbers b_1, b_2, ..., b_{n} - 1, which mean that between islands i and i + 1 there must be used a bridge number b_{i}. 

If there are multiple correct answers, print any of them. Note that in this problem it is necessary to print "Yes" and "No" in correct case.


-----Examples-----
Input
4 4
1 4
7 8
9 10
12 14
4 5 3 8

Output
Yes
2 3 1 

Input
2 2
11 14
17 18
2 9

Output
No

Input
2 1
1 1
1000000000000000000 1000000000000000000
999999999999999999

Output
Yes
1 



-----Note-----

In the first sample test you can, for example, place the second bridge between points 3 and 8, place the third bridge between points 7 and 10 and place the first bridge between points 10 and 14.

In the second sample test the first bridge is too short and the second bridge is too long, so the solution doesn't exist.
"""

import heapq

def can_connect_islands(n, m, islands, bridges):
    # Calculate the gaps between adjacent islands
    gaps = []
    for i in range(n - 1):
        l_i, r_i = islands[i]
        l_next, r_next = islands[i + 1]
        min_gap = l_next - r_i
        max_gap = r_next - l_i
        gaps.append((min_gap, max_gap, i))
    
    # Sort the gaps by their minimum required length
    gaps.sort()
    
    # Sort the bridges with their original indices
    sorted_bridges = sorted((bridge, i) for i, bridge in enumerate(bridges))
    
    # Initialize the result list and a min-heap for bridges
    result = [None] * (n - 1)
    bridge_heap = []
    
    # Index for iterating through the sorted gaps
    gap_index = 0
    
    # Iterate through the sorted bridges
    for bridge, original_index in sorted_bridges:
        # Push all gaps that can be satisfied by the current bridge into the heap
        while gap_index < len(gaps) and gaps[gap_index][0] <= bridge:
            min_gap, max_gap, gap_index_in_original = gaps[gap_index]
            heapq.heappush(bridge_heap, (max_gap, min_gap, gap_index_in_original))
            gap_index += 1
        
        # If there are gaps in the heap, try to satisfy the smallest one
        if bridge_heap:
            max_gap, min_gap, gap_index_in_original = bridge_heap[0]
            if min_gap <= bridge <= max_gap:
                result[gap_index_in_original] = original_index + 1
                heapq.heappop(bridge_heap)
    
    # Check if all gaps have been satisfied
    if None in result:
        return "No"
    else:
        return "Yes", result