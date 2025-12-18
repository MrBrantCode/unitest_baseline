"""
QUESTION:
Jenna is playing a computer game involving a large map with $n$ cities numbered sequentially from $1$ to $n$ that are connected by $m$ bidirectional roads. The game's objective is to travel to as many cities as possible without visiting any city more than once. The more cities the player visits, the more points they earn.

As Jenna's fellow student at Hackerland University, she asks you for help choosing an optimal path. Given the map, can you help her find a path that maximizes her score?

Note: She can start and end her path at any two distinct cities.

Input Format

The first line contains two space-separated integers describing the respective values of $n$ (the number of cities) and $m$ (the number of roads). 

Each line $\boldsymbol{i}$ of the $m$ subsequent lines contains two space-separated integers, $x_i$ and $y_i$, describing a bidirectional road between cities $x_i$ and $y_i$.

Map Generation Algorithm    

The graph representing the map was generated randomly in the following way:

Initially, the graph was empty.
Permutations $p_1,\ldots,p_n$ were chosen uniformly at random among all $n!$ permutations.
For each $i\in\{1,\ldots,n-1\}$, edge $(p_i,p_{i+1})$ was added to the graph.
An additional $m-n+1$ edges were chosen uniformly at random among all possible sets of $m-n+1$ edges which don't intersect with edges added during step $3$.

Constraints

$1\leq n\leq10^4$
$1\leq m\leq10^5$
$1\leq x_i,y_i\leq n$
For $30\%$ of test $n\leq25$ and $m\leq75$.
For $50\%$ of test $n\leq100$ and $m\leq500$.
For $70\%$ of test $n\leq500$ and $m\leq2500$.
It's guaranteed that a valid path of length $n$ always exists. 

Scoring

A valid path of length $\boldsymbol{d}$ earns $(\frac{d}{n})^2\times100\%$ of a test case's available points. The total score will be rounded to next $5\%$.

Output Format

Print the following two lines of output:

The first line must contain a single integer, $\boldsymbol{d}$, denoting the length of the path.
The second line must contain $\boldsymbol{d}$ distinct space-separated integers describing Jenna's path in the same order in which she visited each city.

Sample Input 0
4 5
3 1
3 4
2 4
2 3
4 1

Sample Output 0
4
1 4 2 3

Explanation 0

The diagrams below depict the city's initial map, an optimal path that would earn a full score, and an alternative path that would earn a partial score:

In the optimal path (center image), Jenna walks the path $1\to4\to2\to3$. This answer earns $\textbf{100\%}$ of the maximum score because the path length, $\begin{array}{c}4\end{array}$, is equal to $n$ (i.e., she was able to visit every city exactly once). 

In the alternative path (right image), Jenna walks the path $1\rightarrow4\rightarrow3$ for $(\frac{3}{4})^2\times100\%=\frac{9}{16}\times100\%=56.25\%\Rightarrow60\%$ of the maximum score.
"""

from collections import defaultdict

class Graph(object):

    def __init__(self):
        self._connections = defaultdict(set)

    @property
    def connections(self):
        return self._connections

    @connections.setter
    def connections(self, value):
        self._connections = defaultdict(set)
        self._connections.update(value)

    def copy(self, donor):
        graph_copy = type(self)()
        graph_copy.connections = donor.connections
        return graph_copy

    def add_arc(self, source, destination):
        self._connections[source].add(destination)
        self._connections[destination].add(source)

    def remove_node(self, node):
        for connected_node in self._connections[node]:
            self._connections[connected_node].remove(node)
        del self._connections[node]

def choice(nodes, graph):
    nodes = list(nodes)
    best_choice = None
    best_choice_score = float('inf')
    for node in nodes:
        this_node_score = len(graph._connections[node])
        if this_node_score < best_choice_score:
            best_choice_score = this_node_score
            best_choice = node
    return best_choice

def random_walk(graph):
    current_node = choice(graph._connections.keys(), graph)
    path = []
    while True:
        path.append(current_node)
        choices = graph._connections[current_node]
        if not choices:
            break
        graph.remove_node(current_node)
        next_node = choice(choices, graph)
        current_node = next_node
    return path

def find_optimal_path(n, m, roads):
    graph = Graph()
    for (source, destination) in roads:
        graph.add_arc(source, destination)
    path = random_walk(graph)
    return len(path), path