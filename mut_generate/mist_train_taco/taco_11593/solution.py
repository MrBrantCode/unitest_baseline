"""
QUESTION:
A restaurant received n orders for the rental. Each rental order reserve the restaurant for a continuous period of time, the i-th order is characterized by two time values — the start time l_{i} and the finish time r_{i} (l_{i} ≤ r_{i}).

Restaurant management can accept and reject orders. What is the maximal number of orders the restaurant can accept?

No two accepted orders can intersect, i.e. they can't share even a moment of time. If one order ends in the moment other starts, they can't be accepted both.


-----Input-----

The first line contains integer number n (1 ≤ n ≤ 5·10^5) — number of orders. The following n lines contain integer values l_{i} and r_{i} each (1 ≤ l_{i} ≤ r_{i} ≤ 10^9).


-----Output-----

Print the maximal number of orders that can be accepted.


-----Examples-----
Input
2
7 11
4 7

Output
1

Input
5
1 2
2 3
3 4
4 5
5 6

Output
3

Input
6
4 8
1 5
4 7
2 5
1 3
6 8

Output
2
"""

def max_non_overlapping_orders(orders):
    """
    Calculate the maximal number of non-overlapping orders that can be accepted.

    Parameters:
    orders (list of tuples): A list of tuples where each tuple contains two integers (l, r) representing the start and finish time of an order.

    Returns:
    int: The maximal number of non-overlapping orders that can be accepted.
    """
    # Sort orders by their finish time in ascending order
    sorted_orders = sorted(orders, key=lambda x: x[1])
    
    # Initialize variables to track the maximal number of orders and the end time of the last accepted order
    max_orders = 0
    last_end_time = -1
    
    # Iterate through the sorted orders
    for start, end in sorted_orders:
        if start > last_end_time:
            # If the current order starts after the last accepted order ends, accept it
            max_orders += 1
            last_end_time = end
    
    return max_orders