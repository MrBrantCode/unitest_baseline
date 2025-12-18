"""
QUESTION:
Read problems statements in Mandarin Chinese, Russian and Vietnamese as well. 

Chef likes to play with graphs a lot. Today he created a graph in the following way. He first lays down N nodes in a circle. The nodes nodes are numbered from 1 to N, in the clockwise order, i.e. the node 2 is followed by 1, 3 is followed by 2, and 1 is followed by N. Two vertices are said to be adjacent if they don't have an intermediate vertex placed between them. There is an edge between each adjacent pair of vertices, so there are total N such edges. Each edge has an integer associated with it (may be negative). 

Chef wants to find a walk from node start to node end using the above described edges. Chef has to pay cost for each edge in the walk equal to the integer associated with the edge. He wants to minimize the total cost he will incur. Also, Chef does not like to move through an edge more than twice. Find out minimum cost that Chef has to pay.

Note that a walk from a node u to v can contain repeated vertices in it. Please refer to  link for a formal definition.

------ Input ------ 

The first line of the input contains an integer T denoting the number of test cases. The description of T test cases follows.

The first line of each test case contains a single integer N denoting the number of nodes. 

The second line contains N space-separated integers R_{1}, R_{2}, ..., R_{N} denoting the integer of the rib from node i to node (i % N) + 1. Note that R_{N} is an integer on a rib from node N to node 1. 

The third line contains two integers start and end denoting the first and the last node of the walk. 

------ Output ------ 

For each test case, output a single line containing the minimal possible cost Chef need to pay.

------ Constraints ------ 

$-10^{6} ≤ R_{i} ≤ 10^{6}$
$1 ≤ start < end ≤ N$

------ Subtasks ------ 

$Subtask #1 (20 points): 1 ≤ sum of N ≤ 20; 1 ≤ N ≤ 8$

$Subtask #2 (30 points): 1 ≤ sum of all N ≤ 10^{3}; 1 ≤ N ≤ 200$

$Subtask #3 (50 points): 1 ≤ sum of all N ≤ 10^{6}; 1 ≤ N ≤ 2 × 10^{5} $

----- Sample Input 1 ------ 
2
4
1 2 1 1
1 3
5
-5 100 100 100 2
1 5
----- Sample Output 1 ------ 
2
-8
----- explanation 1 ------ 
Example case 1. Chef's walk starts with node 1. He goes to node 4 by incurring a cost of 1. Then from node 4, he goes to node 3 by incurring a cost of 1 more. Total cost incurred is 2.
Example case 2. Chef goes from 1 to 2 by incurring a cost of -5. Then from 2 to 1 using the edge second time and incurring cost of -5 again. Now, he can not use the edge between 1 and 2 again, as he has traversed the edge already twice. Now he will go from node 1 to node 4 by paying a cost of 2. Total sum of costs incurred is -5 + -5 + 2 = -8. This is the minimum possible cost that Chef can have.
"""

def calculate_min_cost(N, costs, start, end):
    prefix_sum = []
    for cost in costs:
        if len(prefix_sum) > 0:
            prefix_sum.append(prefix_sum[-1] + cost)
        else:
            prefix_sum.append(cost)
    
    U = start - 1
    V = end - 1
    
    j = U
    temp = 0
    sum_1 = 0
    max_sub_1 = 0
    while True:
        sum_1 += costs[j]
        temp += costs[j]
        if temp < 0:
            temp = 0
        max_sub_1 = max(max_sub_1, temp)
        if (j + 1) % N == V:
            break
        j += 1
        j %= N
    
    j = U
    sum_2 = 0
    max_sub_2 = 0
    temp = 0
    j -= 1
    if j < 0:
        j = N - 1
    while True:
        sum_2 += costs[j]
        temp += costs[j]
        if temp < 0:
            temp = 0
        max_sub_2 = max(max_sub_2, temp)
        if j == V:
            break
        j -= 1
        j %= N
    
    ans1 = sum_1 + 2 * (sum_2 - max_sub_2)
    ans2 = sum_2 + 2 * (sum_1 - max_sub_1)
    
    return min(ans1, ans2)