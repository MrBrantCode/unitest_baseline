"""
QUESTION:
This problem is to implement disjoint set union. There will be 2 incomplete functions namely union and find. You have to complete these functions. 
Union: Join two subsets into a single set.
isConnected: Determine which subset a particular element is in. This can be used for determining if two elements are in same subset.
Example 1:
Input:
N = 5
q = 4
Queries = 
Union(1,3)
isConnected(1,2)
Union(1,5)
isConnected(3,5)
Output:
0
1
Explanation: Initially all nodes 1 2 3 4 5
are not connected. 
After Union(1,3), node 1 and 3 will be
connected.
When we do isConnected(1,2),  as node 1
and 2 are not connected it will return 0.
After Union(1,5), node 1 and 5 will be
connected.
When we do isConnected(3,5),  as node
1 and 3 are connected, and node 1 and 5
are connected, hence 3 and 5 are
connected. Thus it will return 1.
Example 2:
Input:
N = 5
q = 4
Queries = 
Union(1,4)
Union(1,5)
isConnected(2,3)
Union(3,4)
Output: 0
Your Task:
You have to complete the function union_() which merges the node1 and node2. You will also have to complete the function isConnected() which will return whether the two nodes are connected.
Note: Both function will contain two arrays par[] and ranks1[] along with two nodes. Initially par[i] = i and rank1[i] = 1 
Expected Time Complexity: O(N + Q).
Expected Auxiliary Space: O(1).
Constraints: 
1 <= N <= 10^{5}
1<= Q <= 10^{5}
1 <= node1, node2 <= N
"""

def disjoint_set_union(N, queries):
    par = list(range(N + 1))
    rank1 = [1] * (N + 1)
    results = []

    def find(r):
        while par[r] != r:
            r = par[r]
        return r

    def compress(x, r):
        while x != r:
            par[x] = r
            x = par[x]

    def union_(a, b):
        r1 = find(a)
        r2 = find(b)
        if r1 != r2:
            if rank1[r1] > rank1[r2]:
                par[r2] = r1
            elif rank1[r1] < rank1[r2]:
                par[r1] = r2
            else:
                par[r1] = r2
                rank1[r2] += 1
        compress(a, r2)
        compress(b, r2)

    def is_connected(x, y):
        return find(x) == find(y)

    for query in queries:
        if query[0] == 'Union':
            union_(query[1], query[2])
        elif query[0] == 'isConnected':
            results.append(int(is_connected(query[1], query[2])))

    return results