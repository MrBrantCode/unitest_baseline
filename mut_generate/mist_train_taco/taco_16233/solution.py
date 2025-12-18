"""
QUESTION:
Cities on a map are connected by a number of roads.  The number of roads between each city is in an array and city ${0}$ is the starting location.  The number of roads from city ${0}$ to city ${1}$ is the first value in the array, from city ${1}$ to city $2$ is the second, and so on.  

How many paths are there from city ${0}$ to the last city in the list, modulo $1234567$?

Example 

$n=4$ 

$routes=[3,4,5]$  

There are $3$ roads to city ${1}$, ${4}$ roads to city $2$ and $5$ roads to city $3$.  The total number of roads is $3\times4\times5\mod1234567=60$. 

Note 

Pass all the towns T_{i} for i=1 to n-1 in numerical order to reach T_{n}.  

Function Description  

Complete the connectingTowns function in the editor below.  

connectingTowns has the following parameters:  

int n: the number of towns  
int routes[n-1]: the number of routes between towns  

Returns  

int: the total number of routes, modulo 1234567. 

Input Format 

The first line contains an integer T, T test-cases follow.   

Each test-case has 2 lines. 

  The first line contains an integer N (the number of towns). 

  The second line contains N - 1 space separated integers where the i^{th} integer denotes the number of routes, N_{i}, from the town T_{i} to T_{i+1}  

Constraints 

1 <= T<=1000

2< N <=100

1 <= routes[i] <=1000

Sample Input  

2
3
1 3
4
2 2 2

Sample Output  

3
8

Explanation 

Case 1: 1 route from T_{1} to T_{2}, 3 routes from T_{2} to T_{3}, hence only 3 routes. 

Case 2: There are 2 routes from each city to the next, hence 2 * 2 * 2 = 8.
"""

def connecting_towns(n, routes):
    total_routes = 1
    for route in routes:
        total_routes *= route
        total_routes %= 1234567
    return total_routes