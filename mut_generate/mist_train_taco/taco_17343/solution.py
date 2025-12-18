"""
QUESTION:
Takeshi, who loves hot springs, is planning a trip to a hot spring resort on his next long vacation. I would like to travel by connecting to a long-distance bus and reach my destination with as little money as possible. Takeshi, who has savings but is unwilling to pay, decided to consult with his grandfather. The grandfather, who was impressed by the plan, gave Takeshi a special ticket.

The ticket was that you could ride two consecutive sections of a long-distance bus only once for free. Depending on how you use it, you can expect a considerable reduction in travel costs, but you need to make a solid plan in order to achieve a greater effect.

A total of n departure points, destinations, and relay points, and m lines connecting the two points are given. Each point is assigned a number from 1 to n. The starting point is 1 and the destination is n. Route information is represented by the two points a and b that connect the route and its fare c. Due to the special ticket validity, you can pass two consecutive lines from any point at no charge. However, passing through the destination on the way does not mean that you have reached the destination.

Create a program that outputs the minimum fare by inputting the total number of departure points, destinations, and relay points n, the number of routes m, and the information of each route. However, there must always be a route from the origin to the destination.



input

Given multiple datasets. The end of the input is indicated by two lines of zeros. Each dataset is given in the following format:


n m
a1 b1 c1
a2 b2 c2
::
am bm cm


The first line gives the total number of origins, destinations, and transit points n (2 ≤ n ≤ 100) and the number of routes m (1 ≤ m ≤ 300). The following m lines give information for each line ai, bi, ci (1 ≤ ci ≤ 1000).

The number of datasets does not exceed 40.

output

Prints the minimum charge on one line for each input dataset.

Example

Input

2 1
1 2 5
3 2
1 2 5
2 3 5
6 9
1 2 7
1 3 9
1 5 14
2 3 10
2 4 15
3 4 11
3 5 2
4 5 9
4 6 8
0 0


Output

5
0
7
"""

def calculate_minimum_fare(n, m, routes):
    MAX_V = 999999999999999999999
    
    # Initialize costs dictionary
    costs = {x: [] for x in range(1, n + 1)}
    
    # Populate costs dictionary with route information
    for (a, b, c) in routes:
        costs[a].append((b, c))
        costs[b].append((a, c))
    
    # Initialize passed and result arrays
    passed = [[False for _ in range(2)] for _ in range(n + 1)]
    result = [MAX_V, MAX_V]
    
    # Initialize the priority queue with the starting point
    spam = [(0, 1, 2)]
    
    while spam:
        mc = min(spam)
        spam.remove(mc)
        tic_i = 0 if mc[2] == 2 else 1
        
        if mc[2] != 1 and passed[mc[1]][tic_i]:
            continue
        
        if mc[2] != 1:
            passed[mc[1]][tic_i] = True
            if n == mc[1]:
                result[tic_i] = mc[0]
        
        if max(result) < MAX_V:
            break
        
        for cv in costs[mc[1]]:
            if mc[2] != 1:
                spam.append((mc[0] + cv[1], cv[0], mc[2]))
            if mc[2] > 0:
                spam.append((mc[0], cv[0], mc[2] - 1))
    
    return min(result)