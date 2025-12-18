"""
QUESTION:
Sagheer is working at a kindergarten. There are n children and m different toys. These children use well-defined protocols for playing with the toys:

  * Each child has a lovely set of toys that he loves to play with. He requests the toys one after another at distinct moments of time. A child starts playing if and only if he is granted all the toys in his lovely set.
  * If a child starts playing, then sooner or later he gives the toys back. No child keeps the toys forever.
  * Children request toys at distinct moments of time. No two children request a toy at the same time.
  * If a child is granted a toy, he never gives it back until he finishes playing with his lovely set.
  * If a child is not granted a toy, he waits until he is granted this toy. He can't request another toy while waiting.
  * If two children are waiting for the same toy, then the child who requested it first will take the toy first.



Children don't like to play with each other. That's why they never share toys. When a child requests a toy, then granting the toy to this child depends on whether the toy is free or not. If the toy is free, Sagheer will give it to the child. Otherwise, the child has to wait for it and can't request another toy.

Children are smart and can detect if they have to wait forever before they get the toys they want. In such case they start crying. In other words, a crying set is a set of children in which each child is waiting for a toy that is kept by another child in the set.

Now, we have reached a scenario where all the children made all the requests for their lovely sets, except for one child x that still has one last request for his lovely set. Some children are playing while others are waiting for a toy, but no child is crying, and no one has yet finished playing. If the child x is currently waiting for some toy, he makes his last request just after getting that toy. Otherwise, he makes the request right away. When child x will make his last request, how many children will start crying?

You will be given the scenario and q independent queries. Each query will be of the form x y meaning that the last request of the child x is for the toy y. Your task is to help Sagheer find the size of the maximal crying set when child x makes his last request.

Input

The first line contains four integers n, m, k, q (1 ≤ n, m, k, q ≤ 105) — the number of children, toys, scenario requests and queries.

Each of the next k lines contains two integers a, b (1 ≤ a ≤ n and 1 ≤ b ≤ m) — a scenario request meaning child a requests toy b. The requests are given in the order they are made by children.

Each of the next q lines contains two integers x, y (1 ≤ x ≤ n and 1 ≤ y ≤ m) — the request to be added to the scenario meaning child x will request toy y just after getting the toy he is waiting for (if any).

It is guaranteed that the scenario requests are consistent and no child is initially crying. All the scenario requests are distinct and no query coincides with a scenario request.

Output

For each query, print on a single line the number of children who will start crying when child x makes his last request for toy y. Please answer all queries independent of each other.

Examples

Input

3 3 5 1
1 1
2 2
3 3
1 2
2 3
3 1


Output

3


Input

5 4 7 2
1 1
2 2
2 1
5 1
3 3
4 4
4 1
5 3
5 4


Output

0
2

Note

In the first example, child 1 is waiting for toy 2, which child 2 has, while child 2 is waiting for top 3, which child 3 has. When child 3 makes his last request, the toy he requests is held by child 1. Each of the three children is waiting for a toy held by another child and no one is playing, so all the three will start crying.

In the second example, at the beginning, child i is holding toy i for 1 ≤ i ≤ 4. Children 1 and 3 have completed their lovely sets. After they finish playing, toy 3 will be free while toy 1 will be taken by child 2 who has just completed his lovely set. After he finishes, toys 1 and 2 will be free and child 5 will take toy 1. Now:

  * In the first query, child 5 will take toy 3 and after he finishes playing, child 4 can play.
  * In the second query, child 5 will request toy 4 which is held by child 4. At the same time, child 4 is waiting for toy 1 which is now held by child 5. None of them can play and they will start crying.
"""

def find_crying_children(n, m, k, q, scenario_requests, queries):
    d = [None] * m
    roots = set(range(n))
    matrix = [[] for _ in range(n)]
    
    for (x, y) in scenario_requests:
        if d[y - 1] is None:
            d[y - 1] = x - 1
        else:
            matrix[d[y - 1]].append(x - 1)
            roots.discard(x - 1)
            d[y - 1] = x - 1
    
    location = [None] * n
    comp_of_conn = []
    graph = [matrix[i][:] for i in range(n)]
    
    for i in roots:
        stack = []
        time = 1
        queue = [[i, time]]
        while queue:
            j = queue[-1]
            time += 1
            if len(graph[j[0]]) == 0:
                stack.append(queue.pop() + [time])
            else:
                queue.append([graph[j[0]].pop(), time])
        stack.reverse()
        if len(stack) > 1:
            for j in range(len(stack)):
                location[stack[j][0]] = [len(comp_of_conn), j]
            for j in range(len(stack) - 1, -1, -1):
                app = 0
                for u in matrix[stack[j][0]]:
                    app += stack[location[u][1]][3]
                stack[j].append(app + 1)
            comp_of_conn.append(stack)
    
    results = []
    for (x, y) in queries:
        x -= 1
        y = d[y - 1]
        if y is None:
            results.append(0)
        elif location[x] is not None and location[y] is not None and location[x][0] == location[y][0]:
            c = location[x][0]
            ind_x = location[x][1]
            ind_y = location[y][1]
            if comp_of_conn[c][ind_x][1] < comp_of_conn[c][ind_y][1] and comp_of_conn[c][ind_x][2] > comp_of_conn[c][ind_y][2]:
                results.append(comp_of_conn[c][ind_x][3])
            else:
                results.append(0)
        else:
            results.append(0)
    
    return results