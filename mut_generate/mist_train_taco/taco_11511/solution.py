"""
QUESTION:
There is a system of n vessels arranged one above the other as shown in the figure below. Assume that the vessels are numbered from 1 to n, in the order from the highest to the lowest, the volume of the i-th vessel is a_{i} liters. [Image] 

Initially, all the vessels are empty. In some vessels water is poured. All the water that overflows from the i-th vessel goes to the (i + 1)-th one. The liquid that overflows from the n-th vessel spills on the floor.

Your task is to simulate pouring water into the vessels. To do this, you will need to handle two types of queries:  Add x_{i} liters of water to the p_{i}-th vessel;  Print the number of liters of water in the k_{i}-th vessel. 

When you reply to the second request you can assume that all the water poured up to this point, has already overflown between the vessels.


-----Input-----

The first line contains integer n — the number of vessels (1 ≤ n ≤ 2·10^5). The second line contains n integers a_1, a_2, ..., a_{n} — the vessels' capacities (1 ≤ a_{i} ≤ 10^9). The vessels' capacities do not necessarily increase from the top vessels to the bottom ones (see the second sample). The third line contains integer m — the number of queries (1 ≤ m ≤ 2·10^5). Each of the next m lines contains the description of one query. The query of the first type is represented as "1 p_{i} x_{i}", the query of the second type is represented as "2 k_{i}" (1 ≤ p_{i} ≤ n, 1 ≤ x_{i} ≤ 10^9, 1 ≤ k_{i} ≤ n).


-----Output-----

For each query, print on a single line the number of liters of water in the corresponding vessel.


-----Examples-----
Input
2
5 10
6
1 1 4
2 1
1 2 5
1 1 4
2 1
2 2

Output
4
5
8

Input
3
5 10 8
6
1 1 12
2 2
1 1 6
1 3 2
2 2
2 3

Output
7
10
5
"""

def simulate_vessels(n, capacities, queries):
    def process_query(node, x, max_capacity, cur_capacity, link):
        i = node
        while link[i] != n + 1 and x > 0:
            if cur_capacity[link[i]] + x < max_capacity[link[i]]:
                cur_capacity[link[i]] += x
                break
            diff = max_capacity[link[i]] - cur_capacity[link[i]]
            cur_capacity[link[i]] = max_capacity[link[i]]
            x -= diff
            link[i] = link[i + 1]
            i = link[i]
        link[node] = link[i]

    def convert_to_dict(max_capacity):
        mydict1, mydict2 = dict(), dict()
        link = dict()
        for i in range(len(max_capacity)):
            mydict1[i + 1] = max_capacity[i]
            mydict2[i + 1] = 0
            link[i + 1] = i + 1
        mydict1[len(max_capacity) + 1] = float('inf')
        mydict2[len(max_capacity) + 1] = float('inf')
        link[len(max_capacity) + 1] = len(max_capacity) + 1
        return mydict1, mydict2, link

    max_capacity, cur_capacity, link = convert_to_dict(capacities)
    results = []

    for query in queries:
        if query[0] == 1:
            process_query(query[1], query[2], max_capacity, cur_capacity, link)
        elif query[0] == 2:
            results.append(cur_capacity[query[1]])

    return results