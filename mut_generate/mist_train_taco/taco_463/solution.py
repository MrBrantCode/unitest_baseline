"""
QUESTION:
Chandan is a horrendous murderer and he wants to kill Arjit just because he's lazy.  Chandan is following the trail of Arjit's shoes. The trail is in the form of a k-ary tree. Arjit is lazy, sure, but he's smart. So, he magically moves away from Chandan as far as he can go.

Chandan doesn't know the way out, but he knows that Arjit has managed to travel the maximum distance he can. Help Chandan find out the maximum distance he would have to travel to find Arjit. And also tell him how much will he have to pay to travel so far. The travel rates are:
If maximum distance is <100, cost = 0.  
If maximum distance is > 100, cost = 100.  
If maximum distance is > 1000, cost = 1000.  
If maximum distance is > 10000, cost = 10000.

Input format:
First line contains the total number of test cases. Then, the next line contains the number of nodes. The the next n lines contain three integers - the first two denote an edge between a and b, the third integer denotes the weight of that edge.  

Output format:
You've to print the money Chandan will pay and the maximum distance he will have to travel.  

Constraints:
1 ≤ Test Cases ≤ 10
2 ≤ n ≤ 100000
1 ≤ a, b ≤ n
1 ≤ weight ≤ 100  

SAMPLE INPUT
1
5
1 2 4
3 2 3
2 5 2
4 1 1

SAMPLE OUTPUT
0 8
"""

def calculate_max_distance_and_cost(test_cases):
    def bfs(x, n, G):
        b = [False] * (n + 1)  # an array of false flags to keep track of vertices visited
        memo = ["p"] * (n + 1)
        l = 0
        c = 0
        q = []
        q.append(x)
        memo[x] = 0
        while q:
            top = q.pop(0)
            b[top] = True
            for j in G[top]:
                if memo[j[0]] == "p":
                    q.append(j[0])
                    memo[j[0]] = memo[top] + j[1]  # time of discovery(level) of child is time of discovery(level) of parent + 1
                    b[j[0]] = True
                    if memo[j[0]] > l:
                        l = memo[j[0]]
                        c = j[0]
        return l, c

    results = []
    for test_case in test_cases:
        n, edges = test_case
        G = [[] for _ in range(n + 1)]
        for x, y, z in edges:
            G[x].append((y, z))  # undirected graph has edge from u to v.
            G[y].append((x, z))  # also has edge from v to u.

        upto, new = bfs(1, n, G)
        found = False
        while not found:
            j = bfs(new, n, G)
            if upto < j[0]:
                upto = j[0]
                new = j[1]
            else:
                found = True

        if upto < 100:
            cost = 0
        elif upto < 1000:
            cost = 100
        elif upto < 10000:
            cost = 1000
        else:
            cost = 10000

        results.append((cost, upto))

    return results