"""
QUESTION:
Read problems statements in Mandarin Chinese  and Russian. 

Time flies fast, Chef’s sons are getting older, stronger and higher. Chef has got two sons and they don’t go well with each other. Their relations are getting worse day by day. Concerned Chef has now decided to separate them. Chef is very rich and he has got N cities (N is even). His sons are all he has and he must divide the cities into his sons equally.  There are some roads running between the cities. Chef has to destruct all the roads between cities of first and second sons. The destruction of road costis a lot of money. So Chef wants to save as much as he can. So you have to help Chef in finding out minimal cost to split cities to his sons.

------ Input ------ 

First line contains two space separated integers N, M denoting the number of cities and the number of the roads respectively. 

Each i^{th} of the following M lines contains three integers a_{i}, b_{i} and c_{i} denoting the road between the city with the number a_{i} and the city with the number b_{i}. The cost for it's destruction is c_{i}.  

------ Output ------ 

In a single line, output N / 2 numbers – the numbers of cities that will belong to the first son after the partition.

------ Scoring ------ 

Your score will be sum of all c_{i} of all edges that would be destroyed by Chef. Your score for the problem will be sum of scores for each test files.
Your solution will be tested against only on 20% of the test files during the contest and will be rejudged against 100% after the end of competition.

------ Constraints ------ 

$1 ≤ N ≤ 10^{6}$
$1 ≤ M ≤ 10^{6}$
$0 ≤ a_{i}, b_{i} < N$
$1 ≤ c_{i} ≤ 10^{9}$

------ Subtasks ------ 

Subtask 1:

$1 ≤ N ≤ 100$
$1 ≤ M ≤ 1000$

Subtask 2:

$100 ≤ N ≤ 2*10^{4}$
$1000 ≤ M ≤ 2*10^{5}$

Subtask 3:

$2*10^{4} ≤ N ≤ 10^{5}$
$2*10^{5} ≤ M ≤ 4*10^{5}$

Subtask 4:

$10^{5} ≤ N ≤ 10^{6}$
$4*10^{5} ≤ M ≤ 10^{6}$

------ Example ------ 

Input:
4 4
0 1 1 
1 2 2
2 3 3
3 0 4

Output:
1 2

------ Test data generation ------ 

Four plans are used:

$Complete graph with random edge weights$
$Complete bipartite graph with random edge weights$
$Random tree$
$Fully random graph$

The first two sections subtasks are generated with the usage of all 4 of them, third section is generated with the usage only of the fourth plan, and fourth section is generated with the plans number 3 and 4.
"""

from random import sample

def minimal_cost_partition(N, M, roads):
    # Generate a random sample of N/2 cities for the first son
    first_son_cities = sample(range(1, N), N >> 1)
    
    # Return the list of cities for the first son
    return first_son_cities