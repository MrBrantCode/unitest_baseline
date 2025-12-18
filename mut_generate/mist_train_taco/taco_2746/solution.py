"""
QUESTION:
Now After eliminating the invalid registrations they are planning to form connections to the participants laptops. The connection can be direct or indirect form and there should be only one connection exists between them. After setting the connections management wanted to know the laptops are connected or not. This problem is assigned to you find out the connections between them. 

There can be two types of connections i.e., direct connection and indirect connection. If the two laptops are connected directly then it is said to be direct connection and the other way is indirect connection.

INPUT:
First line contains a number n which will describe how many laptops are present.
Next line contains no of connections C
next C lines tells you how they are connected
After mentioning connections, Next line has no of queries Q
Next q lines have two points first is the source and second is destination

OUTPUT:
For every query print "Direct Connection"(without quotes) if they are connected directly, print "Indirect Connection" if they are connected indirectly otherwise print "No Connection"

SAMPLE INPUT
4
2
1 2
2 3
3
1 2
1 3
1 4

SAMPLE OUTPUT
Direct Connection
Indirect Connection
No Connection
"""

def check_connection(n, connections, queries):
    # Build the graph
    graph = {i: [] for i in range(1, n + 1)}
    for a, b in connections:
        graph[a].append(b)
        graph[b].append(a)
    
    def find(x, y):
        if x in graph[y]:
            return True
        else:
            for i in graph[y]:
                if find(x, i):
                    return True
            return False
    
    results = []
    for a, b in queries:
        if b in graph[a]:
            results.append('Direct Connection')
        else:
            if find(a, b):
                results.append('Indirect Connection')
            else:
                results.append('No Connection')
    
    return results