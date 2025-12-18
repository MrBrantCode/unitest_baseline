"""
QUESTION:
Cluster analysis - Unweighted pair-group average

Clustering is a task of grouping a set of objects in such a way that the objects in the same class are similar to each other and the objects in different classes are distinct. Cluster analysis is employed in many fields such as machine learning, pattern recognition, image analysis, etc.

In this kata, your task is to implement a simple clustering technique called 'Unweighted pair-group average'. This method takes a set of 2D points and the desired number of final clusters. Initially, each point forms its own cluster. The most similar (least distant) clusters are iteratively merged until the target number of clusters is reached.

The distance metric between two clusters is defined as the average distance between all pairs of points from the two clusters. For example: 
```
Cluster 1: (0, 0), (0, 1)
Cluster 2: (4, 3)
Distance = (sqrt((0-4)^2 + (0-3)^2) + sqrt((0-4)^2 + (1-2)^2)) / 2
```

Input:
- ```points``` - a list of 2D points ```[(1, 1), (3, 5), (4, 4), (8, 2), (0, 1)]```
- ```n``` - the desired number of clusters

Output:
- list of clusters, each cluster is a list of points
- points in each cluster should be sorted in ascending order
- the list of clusters should also be sorted in ascending order

Example:
- ```cluster(3, [(1, 1), (3, 5), (4, 4), (8, 2), (0, 1)])```
- should return 
```[ [(0, 1), (1, 1)],
     [(3, 5), (4, 4)],
     [(8, 2)]
   ]
```
   
Notes:
- the coordinates ```(x, y)``` are chosen from interval ```<0, 1000>```
- ```0 < len(points) <= 100```
- ```0 < n <= len(points)```
- there is always only one unique solution
- there are no duplicate points in the input
"""

from itertools import combinations, product, starmap
import numpy as np

# Memoization dictionaries
memo_points = {}
memo_clusters = {}

def point_dist(p1, p2):
    """Calculate the Euclidean distance between two points."""
    key = (p1, p2) if p1 < p2 else (p2, p1)
    if key not in memo_points:
        memo_points[key] = np.linalg.norm(np.array(key[0]) - np.array(key[1]))
    return memo_points[key]

def cluster_dist(clusters):
    """Calculate the average distance between all pairs of points from two clusters."""
    key = tuple(map(tuple, clusters))
    if key not in memo_clusters:
        memo_clusters[key] = np.mean(list(starmap(point_dist, product(*key))))
    return memo_clusters[key]

def unweighted_pair_group_average_clustering(points, n):
    """Perform Unweighted Pair-Group Average clustering on a set of 2D points."""
    clusters = [[p] for p in points]
    while len(clusters) > n:
        # Find the pair of clusters with the minimum average distance
        (c1, c2) = min(combinations(clusters, 2), key=cluster_dist)
        # Merge the two clusters
        c1.extend(c2)
        clusters.remove(c2)
    # Sort points within each cluster and the clusters themselves
    return sorted(map(sorted, clusters))