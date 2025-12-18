"""
QUESTION:
A factory produces thimbles in bulk. Typically, it can produce up to a thimbles a day. However, some of the machinery is defective, so it can currently only produce b thimbles each day. The factory intends to choose a k-day period to do maintenance and construction; it cannot produce any thimbles during this time, but will be restored to its full production of a thimbles per day after the k days are complete.

Initially, no orders are pending. The factory receives updates of the form d_{i}, a_{i}, indicating that a_{i} new orders have been placed for the d_{i}-th day. Each order requires a single thimble to be produced on precisely the specified day. The factory may opt to fill as many or as few of the orders in a single batch as it likes.

As orders come in, the factory owner would like to know the maximum number of orders he will be able to fill if he starts repairs on a given day p_{i}. Help the owner answer his questions.


-----Input-----

The first line contains five integers n, k, a, b, and q (1 ≤ k ≤ n ≤ 200 000, 1 ≤ b < a ≤ 10 000, 1 ≤ q ≤ 200 000) — the number of days, the length of the repair time, the production rates of the factory, and the number of updates, respectively.

The next q lines contain the descriptions of the queries. Each query is of one of the following two forms:   1 d_{i} a_{i} (1 ≤ d_{i} ≤ n, 1 ≤ a_{i} ≤ 10 000), representing an update of a_{i} orders on day d_{i}, or  2 p_{i} (1 ≤ p_{i} ≤ n - k + 1), representing a question: at the moment, how many orders could be filled if the factory decided to commence repairs on day p_{i}? 

It's guaranteed that the input will contain at least one query of the second type.


-----Output-----

For each query of the second type, print a line containing a single integer — the maximum number of orders that the factory can fill over all n days.


-----Examples-----
Input
5 2 2 1 8
1 1 2
1 5 3
1 2 1
2 2
1 4 2
1 3 2
2 1
2 3

Output
3
6
4

Input
5 4 10 1 6
1 1 5
1 5 5
1 3 2
1 5 2
2 1
2 2

Output
7
1



-----Note-----

Consider the first sample.

We produce up to 1 thimble a day currently and will produce up to 2 thimbles a day after repairs. Repairs take 2 days.

For the first question, we are able to fill 1 order on day 1, no orders on days 2 and 3 since we are repairing, no orders on day 4 since no thimbles have been ordered for that day, and 2 orders for day 5 since we are limited to our production capacity, for a total of 3 orders filled.

For the third question, we are able to fill 1 order on day 1, 1 order on day 2, and 2 orders on day 5, for a total of 4 orders.
"""

def calculate_max_orders(n, k, a, b, q, queries):
    def add(arr, x, v):
        while x < len(arr):
            arr[x] += v
            x |= x + 1

    def get(arr, x):
        r = 0
        while x >= 0:
            r += arr[x]
            x = (x & x + 1) - 1
        return r

    h1 = [0] * n
    h2 = [0] * n
    z = [0] * n
    results = []

    for t in queries:
        if t[0] == 1:
            d_i, a_i = t[1], t[2]
            p = z[d_i - 1]
            pp = p + a_i
            add(h1, d_i - 1, min(a, pp) - min(a, p))
            add(h2, d_i - 1, min(b, pp) - min(b, p))
            z[d_i - 1] = pp
        elif t[0] == 2:
            p_i = t[1]
            result = get(h2, p_i - 2) + get(h1, n - 1) - get(h1, p_i + k - 2)
            results.append(result)

    return results