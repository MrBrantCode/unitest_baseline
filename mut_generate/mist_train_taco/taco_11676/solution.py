"""
QUESTION:
Little boy Gerald studies at school which is quite far from his house. That's why he has to go there by bus every day. The way from home to school is represented by a segment of a straight line; the segment contains exactly n + 1 bus stops. All of them are numbered with integers from 0 to n in the order in which they follow from Gerald's home. The bus stop by Gerald's home has number 0 and the bus stop by the school has number n.

There are m buses running between the house and the school: the i-th bus goes from stop si to ti (si < ti), visiting all the intermediate stops in the order in which they follow on the segment. Besides, Gerald's no idiot and he wouldn't get off the bus until it is still possible to ride on it closer to the school (obviously, getting off would be completely pointless). In other words, Gerald can get on the i-th bus on any stop numbered from si to ti - 1 inclusive, but he can get off the i-th bus only on the bus stop ti.

Gerald can't walk between the bus stops and he also can't move in the direction from the school to the house.

Gerald wants to know how many ways he has to get from home to school. Tell him this number. Two ways are considered different if Gerald crosses some segment between the stops on different buses. As the number of ways can be too much, find the remainder of a division of this number by 1000000007 (109 + 7).

Input

The first line contains two space-separated integers: n and m (1 ≤ n ≤ 109, 0 ≤ m ≤ 105). Then follow m lines each containing two integers si, ti. They are the numbers of starting stops and end stops of the buses (0 ≤ si < ti ≤ n).

Output

Print the only number — the number of ways to get to the school modulo 1000000007 (109 + 7).

Examples

Input

2 2
0 1
1 2


Output

1


Input

3 2
0 1
1 2


Output

0


Input

5 5
0 1
0 2
0 3
0 4
0 5


Output

16

Note

The first test has the only variant to get to school: first on bus number one to the bus stop number one; then on bus number two to the bus stop number two.

In the second test no bus goes to the third bus stop, where the school is positioned. Thus, the correct answer is 0.

In the third test Gerald can either get or not on any of the first four buses to get closer to the school. Thus, the correct answer is 24 = 16.
"""

def count_ways_to_school(n, m, buses):
    MOD = 10**9 + 7
    
    if m == 0:
        return 0
    
    # Collect all unique stops
    stops_set = set()
    for (start, end) in buses:
        stops_set.add(start)
        stops_set.add(end)
    stops_set.add(0)
    stops_set.add(n)
    
    # Sort the stops and create a mapping from stop to index
    stops = sorted(list(stops_set))
    stop_to_index = {stop: idx for idx, stop in enumerate(stops)}
    
    # Convert bus routes to use the new indices
    indexed_buses = [(stop_to_index[start], stop_to_index[end]) for (start, end) in buses]
    indexed_buses.sort(key=lambda x: x[1])
    
    # Initialize arrays for dynamic programming
    num_stops = len(stops) - 1
    ways = [0] * (num_stops + 1)
    cumulative_ways = [0] * (num_stops + 2)
    
    ways[0] = 1
    
    j = 0
    for i in range(num_stops + 1):
        while j < m and indexed_buses[j][1] == i:
            start, end = indexed_buses[j]
            ways[end] += cumulative_ways[end] - cumulative_ways[start]
            j += 1
        cumulative_ways[i + 1] = (cumulative_ways[i] + ways[i]) % MOD
    
    return ways[num_stops] % MOD