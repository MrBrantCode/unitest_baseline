"""
QUESTION:
The professional Russian, Dmitri, from the popular youtube channel FPSRussia has hired you to help him move his arms cache between locations without detection by the authorities.  Your job is to write a Shortest Path First (SPF) algorithm that will provide a route with the shortest possible travel time between waypoints, which will minimize the chances of detection.  One exception is that you can't travel through the same waypoint twice.  Once you've been seen there is a higher chance of detection if you travel through that waypoint a second time.

Your function shortestPath will take three inputs, a topology/map of the environment, along with a starting point, and an ending point.  The topology will be a dictionary with the keys being the different waypoints.  The values of each entry will be another dictionary with the keys being the adjacent waypoints, and the values being the time it takes to travel to that waypoint.

Take the following topology as an example:

     topology = {'a' : {'b': 10, 'c': 20},
                 'b' : {'a': 10, 'c': 20},
                 'c' : {'a': 10, 'b': 20} }

In this example, waypoint 'a' has two adjacent waypoints, 'b' and 'c'.  And the time it takes to travel from 'a' to 'b' is 10 minutes, and from 'a' to 'c' is 20 minutes.  It's important to note that the time between these waypoints is one way travel time and can be different in opposite directions.  This is highlighted in the example above where a->c takes 20 minutes, but c->a takes 10 minutes.

The starting and ending points will passed to your function as single character strings such as 'a' or 'b', which will match a key in your topology.

The return value should be in the form of a list of lists of waypoints that make up the shortest travel time.  If there multiple paths that have equal travel time, then you should choose the path with the least number of waypoints.  If there are still multiple paths with equal travel time and number of waypoints, then you should return a list of lists with the multiple options. For multiple solutions, the list of paths should be sorted in lexicographic (alphabetical) order. If there is only one shortest path, you should still return a list of that list.

Here are a few examples:
    #Topology
    #      b--d--g   
    #     /   |   \  
    #    /    |    \ 
    #   a-----e     h
    #    \     \   / 
    #     \     \ /  
    #      c-----f  
    topology = {'a' : {'b': 10, 'c': 20, 'e':20},
                'b' : {'a': 10, 'd': 20},
                'c' : {'a': 10, 'f': 20},
                'd' : {'b': 10, 'e': 20, 'g': 20},
                'e' : {'a': 10, 'd': 20, 'f': 20},                      
                'f' : {'c': 10, 'e': 20, 'h': 20},
                'g' : {'d': 10, 'h': 20},
                'h' : {'g': 10, 'f': 20},
    }
    
    Two solutions with a time of 40:
    shortestPath(topology, 'a', 'f') == [['a', 'c', 'f'], ['a', 'e', 'f']] 
     
    One solution with a time of 20:
    shortestPath(topology, 'a', 'e') == [['a', 'e']]
"""

from collections import defaultdict

def find_shortest_paths(topology, start, end):
    (Q, paths, d) = ([[0, start]], [], defaultdict(list))
    while Q:
        vrt = Q.pop(0)
        if vrt[-1] == end:
            paths.append(vrt)
            continue
        for (v, c) in topology[vrt[-1]].items():
            if v not in vrt:
                Q.append([vrt[0] + c] + vrt[1:] + [v])
    for i in paths:
        d[i[0]].append(i[1:])
    (ml, f) = (len(min(d[min(d)], key=len)), [])
    for i in d[min(d)]:
        if len(i) == ml:
            f.append(i)
    return [sorted(i) for i in f] if len(f) > 1 else f