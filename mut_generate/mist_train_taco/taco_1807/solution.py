"""
QUESTION:
Lindsey Buckingham told Stevie Nicks "Go your own way". Nicks is now sad and wants to go away as quickly as possible, but she lives in a 2D hexagonal world.

Consider a hexagonal tiling of the plane as on the picture below. [Image] 

Nicks wishes to go from the cell marked $(0, 0)$ to a certain cell given by the coordinates. She may go from a hexagon to any of its six neighbors you want, but there is a cost associated with each of them. The costs depend only on the direction in which you travel. Going from $(0, 0)$ to $(1, 1)$ will take the exact same cost as going from $(-2, -1)$ to $(-1, 0)$. The costs are given in the input in the order $c_1$, $c_2$, $c_3$, $c_4$, $c_5$, $c_6$ as in the picture below. [Image] 

Print the smallest cost of a path from the origin which has coordinates $(0, 0)$ to the given cell.


-----Input-----

Each test contains multiple test cases. The first line contains the number of test cases $t$ ($1 \le t \le 10^{4}$). Description of the test cases follows.

The first line of each test case contains two integers $x$ and $y$ ($-10^{9} \le x, y \le 10^{9}$) representing the coordinates of the target hexagon.

The second line of each test case contains six integers $c_1$, $c_2$, $c_3$, $c_4$, $c_5$, $c_6$ ($1 \le c_1, c_2, c_3, c_4, c_5, c_6 \le 10^{9}$) representing the six costs of the making one step in a particular direction (refer to the picture above to see which edge is for each value).


-----Output-----

For each testcase output the smallest cost of a path from the origin to the given cell.


-----Example-----
Input
2
-3 1
1 3 5 7 9 11
1000000000 1000000000
1000000000 1000000000 1000000000 1000000000 1000000000 1000000000

Output
18
1000000000000000000



-----Note-----

The picture below shows the solution for the first sample. The cost $18$ is reached by taking $c_3$ 3 times and $c_2$ once, amounting to $5+5+5+3=18$. [Image]
"""

def calculate_minimum_cost(x, y, costs):
    # Extend the costs list to handle wrap-around cases
    extended_costs = costs + costs + costs
    
    # Apply the optimization step multiple times
    for _ in range(20):
        for i in range(1, 16):
            extended_costs[i] = min(extended_costs[i], extended_costs[i - 1] + extended_costs[i + 1])
    
    # Extract the optimized costs
    c1, c2, c3, c4, c5, c6 = extended_costs[6:12]
    
    # Calculate the minimum cost based on the quadrant of the target hexagon
    if x >= 0 and y >= 0:
        mm = min(x, y)
        x -= mm
        y -= mm
        return mm * c1 + y * c2 + x * c6
    elif x >= 0 and y < 0:
        return abs(y) * c5 + x * c6
    elif x < 0 and y < 0:
        x, y = abs(x), abs(y)
        mm = min(x, y)
        x -= mm
        y -= mm
        return mm * c4 + y * c5 + x * c3
    else:
        return abs(y) * c2 + abs(x) * c3