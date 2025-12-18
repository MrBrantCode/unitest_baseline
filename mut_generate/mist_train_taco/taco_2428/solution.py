"""
QUESTION:
Monk was asked to answer some queries in an interview. He is given an empty array A. Queries are of 4 types:-
1. 1 X - Add number X to the array A.
2. 2 X - Remove a single instance of number X from the array A. If not possible, print "-1" without the quotes.
3. 3 - Find the maximum element in the array A.
4. 4 - Find the minimum element in the array A.  

Input:
The first line contains the integer Q.
The next Q lines will each contain a query like the ones mentioned above.

Output: 
For queries 3 and 4, print the answer in a new line. If the array is empty for query 3 and 4, then print "-1" without the quotes.

Constraints:
1 ≤ Q ≤ 100000
1 ≤ X ≤ 100000

SAMPLE INPUT
5
1 5
1 9
1 6
3
2 1

SAMPLE OUTPUT
9
-1

Explanation

There are 5 queries.
Query 1 - 5 is added to the array.
Query 2 - 9 is added to the array.
Query 3 - 6 is added to the array.
Query 4 - The maximum element in the array is 9.
Query 5 - Since there is no element in the array with value 1, so the output is -1.
"""

import collections
import heapq

def process_queries(queries):
    """
    Process a list of queries on an array and return the results of queries 3 and 4.

    Parameters:
    queries (list of lists): A list where each element is a list representing a query.
                             Each query list contains two integers:
                             - The first integer is the type of query (1, 2, 3, or 4).
                             - The second integer (if applicable) is the value X.

    Returns:
    list of str: A list of strings where each string is the result of a query 3 or 4.
                 If the array is empty for query 3 or 4, the result is "-1".
    """
    res = []
    counts = collections.defaultdict(lambda: 0)
    min_q = []
    max_q = []
    
    for query in queries:
        if query[0] == 1:
            counts[query[1]] += 1
            heapq.heappush(min_q, query[1])
            heapq.heappush(max_q, -query[1])
        elif query[0] == 2:
            if not counts[query[1]]:
                res.append("-1")
            else:
                counts[query[1]] -= 1
        elif query[0] == 3:
            while len(max_q) and not counts[-max_q[0]]:
                heapq.heappop(max_q)
            if len(max_q):
                res.append(str(-max_q[0]))
            else:
                res.append("-1")
        elif query[0] == 4:
            while len(min_q) and not counts[min_q[0]]:
                heapq.heappop(min_q)
            if len(min_q):
                res.append(str(min_q[0]))
            else:
                res.append("-1")
    
    return res