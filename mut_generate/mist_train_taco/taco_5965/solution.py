"""
QUESTION:
In this problem at each moment you have a set of intervals. You can move from interval (a, b) from our set to interval (c, d) from our set if and only if c < a < d or c < b < d. Also there is a path from interval I_1 from our set to interval I_2 from our set if there is a sequence of successive moves starting from I_1 so that we can reach I_2.

Your program should handle the queries of the following two types:  "1 x y" (x < y) — add the new interval (x, y) to the set of intervals. The length of the new interval is guaranteed to be strictly greater than all the previous intervals. "2 a b" (a ≠ b) — answer the question: is there a path from a-th (one-based) added interval to b-th (one-based) added interval? 

Answer all the queries. Note, that initially you have an empty set of intervals.


-----Input-----

The first line of the input contains integer n denoting the number of queries, (1 ≤ n ≤ 100). Each of the following lines contains a query as described above. All numbers in the input are integers and don't exceed 10^9 by their absolute value.

It's guaranteed that all queries are correct.


-----Output-----

For each query of the second type print "YES" or "NO" on a separate line depending on the answer.


-----Examples-----
Input
5
1 1 5
1 5 11
2 1 2
1 2 9
2 1 2

Output
NO
YES
"""

def process_interval_queries(queries):
    class Pair:
        def __init__(self, x=0, y=0):
            self.x = x
            self.y = y
            self.neighbors = []
            self.visited = False

    def is_median(pair1, pair2):
        if pair1.x > pair2.x and pair1.x < pair2.y:
            return True
        elif pair1.y > pair2.x and pair1.y < pair2.y:
            return True
        else:
            return False

    def dfs(start_pair, targ_pair):
        stack = [start_pair]
        while stack:
            curr_pair = stack.pop()
            if curr_pair.visited:
                continue
            curr_pair.visited = True
            if curr_pair.x == targ_pair.x and curr_pair.y == targ_pair.y:
                return True
            for neighbor in curr_pair.neighbors:
                stack.append(neighbor)
        return False

    pairs = {}
    count = 0
    results = []

    for query in queries:
        query_type, first, second = query
        if query_type == 1:
            new_pair = Pair(first, second)
            for key in pairs:
                if is_median(new_pair, pairs[key]):
                    new_pair.neighbors.append(pairs[key])
                if is_median(pairs[key], new_pair):
                    pairs[key].neighbors.append(new_pair)
            pairs[count] = new_pair
            count += 1
        elif query_type == 2:
            first_pair = pairs[first - 1]
            second_pair = pairs[second - 1]
            for key in pairs:
                pairs[key].visited = False
            if dfs(first_pair, second_pair):
                results.append('YES')
            else:
                results.append('NO')

    return results