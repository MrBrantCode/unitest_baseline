"""
QUESTION:
It's almost summertime, so Big Cat and Little Cat are getting in shape. They decide the core of their fitness plan is to start jogging every day.

Their city consists of $N$ intersections connected by $\mbox{M}$ bidirectional roads. The cats decide that their jogging route should be cyclic (i.e., starting and ending at the same intersection) and consist of $4$ different roads.

The cats also love exploring new places, so each day they want to choose a new route to jog on that is not equal to any of their previous routes. Two routes are considered to be equal if their sets of component roads are equal.

Given a map of the city, can you help our heroic cats determine the maximum number of days they can go jogging so that every route traveled is different? 

Input Format

The first line contains a pair of space-separated integers, $N$ (the number of intersections) and $\mbox{M}$ (the number of roads), respectively.

Each line $\boldsymbol{i}$ of the $\mbox{M}$ subsequent lines contains a pair of space-separated integers, $X_i$ and $Y_i$, defining a bidirectional road connecting intersections $X_i$ and $Y_i$.

Constraints

$1\leq N\leq5\cdot10^4$
$1\leq M\leq10^5$
$1\leq X_i,Y_i\leq N$
Each bidirectional road connects $2$ distinct intersections (i.e., no road connects an intersection to itself).
Each pair of intersections is directly connected by no more than $1$ road.

Output Format

Print the maximum number of days for which the cats can go jogging without repeating a route.

Sample Input
4 6
1 2
2 3
3 4
4 1
1 3
2 4

Sample Output
3

Explanation

There are $3$ different routes:

$1\to2\to3\to4\to1$
$1\to3\to2\to4\to1$
$1\to2\to4\to3\to1$

Recall that each route is a set of intersections forming a cycle, so each unique route is the same regardless of which city on the route the cats start out at. Thus, we print $3$ (the number of routes) as our answer.
"""

def calculate_max_jogging_days(n, m, graph):
    result = 0
    visited = set([])
    
    for source, destinations in graph.items():
        destination_count = {}
        
        for x in destinations:
            if x not in visited and x in graph:
                for y in graph[x]:
                    if y not in visited:
                        try:
                            destination_count[y] += 1
                        except:
                            destination_count[y] = 1
        
        for node, count in destination_count.items():
            if node != source:
                result += count * (count - 1) // 2
        
        visited.add(source)
    
    return result