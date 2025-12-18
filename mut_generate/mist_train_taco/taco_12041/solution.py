"""
QUESTION:
problem

AOR Ika likes rooted trees with a fractal (self-similar) structure. Consider using the weighted rooted tree $ T $ consisting of $ N $ vertices to represent the rooted tree $ T'$ with the following fractal structure.

* $ T'$ is the addition of a tree rooted at $ x $ and having a tree structure similar to $ T $ (same cost) for each vertex $ x $ of $ T $.
* The root of $ T'$ is the same as that of $ T $.



The tree represented in this way is, for example, as shown in the figure below.

<image>

AOR Ika is trying to do a depth-first search for $ T'$, but finds that it takes a lot of time to trace all the vertices. Therefore, we decided to skip some node visits by performing a depth-first search with a policy of transitioning with a probability of $ p $ and not transitioning with a probability of $ 1-p $ at the time of transition during a depth-first search. Given $ T $ and the probability $ p $, find the expected value of the sum of the costs of all edges to follow when performing a depth-first search for $ T'$. The information of $ T $ is given by the number of vertices $ N $ and the information of the edges of $ N-1 $, and the vertex $ 1 $ is the root. Each vertex is labeled $ 1,2, \ dots, N $, and the $ i \ (1 \ le i \ le N-1) $ th edge costs the vertices $ x_i $ and $ y_i $ $ c_i $ It is tied with. The non-deterministic algorithm of the depth-first search that transitions to a child with a probability of $ p $, which is dealt with in this problem, is expressed as follows. The sum of the costs of the edges that the output $ \ mathrm {answer} $ follows.

1. Prepare an empty stack $ S $.
2. Set $ ​​\ mathrm {answer} = 0 $
3. Push the root vertex of $ T'$ to $ S $.
4. Extract the first element of $ S $ and make it $ x $.
5. For each child $ c $ of $ x $, do the following with probability $ p $ and do nothing with probability $ 1-p $.
* Add vertex $ c $ to $ S $. Then add the weight of the edge connecting $ x $ to $ c $ to $ \ mathrm {answer} $.
6. If S is not empty, transition to 3.
7. Output $ \ mathrm {answer} $.



output

Print the answer in one line. If the relative or absolute error is less than $ 10 ^ {-6} $, then AC. Also, output a line break at the end.

Example

Input

0.75
4
1 2 1
2 3 3
3 4 10


Output

24.8569335938
"""

import collections

def calculate_expected_cost(p, n, edges):
    # Create a dictionary to store the adjacency list of the tree
    d = collections.defaultdict(list)
    
    # Populate the adjacency list with edges and their costs
    for (x, y, c) in edges:
        d[x - 1].append((y - 1, c))
        d[y - 1].append((x - 1, c))
    
    # Initialize the list to store the depth and cost information for each vertex
    f = [None] * n
    f[0] = (0, 0)
    
    # Perform a BFS to calculate the depth and cost for each vertex
    q = [(0, 0)]
    while q:
        (x, b) = q[0]
        q = q[1:]
        for (y, c) in d[x]:
            if f[y] is None:
                q.append((y, b + 1))
                f[y] = (b + 1, c)
    
    # Calculate the expected sum of costs
    s = 0
    for (b, c) in f:
        s += p ** b * c
    
    r = s
    for (b, c) in f:
        r += p ** b * s
    
    return r