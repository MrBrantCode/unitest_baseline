"""
QUESTION:
There is a country with n citizens. The i-th of them initially has a_{i} money. The government strictly controls the wealth of its citizens. Whenever a citizen makes a purchase or earns some money, they must send a receipt to the social services mentioning the amount of money they currently have.

Sometimes the government makes payouts to the poor: all citizens who have strictly less money than x are paid accordingly so that after the payout they have exactly x money. In this case the citizens don't send a receipt.

You know the initial wealth of every citizen and the log of all events: receipts and payouts. Restore the amount of money each citizen has after all events.

Input

The first line contains a single integer n (1 ≤ n ≤ 2 ⋅ 10^{5}) — the numer of citizens.

The next line contains n integers a_1, a_2, ..., a_n (0 ≤ a_{i} ≤ 10^{9}) — the initial balances of citizens.

The next line contains a single integer q (1 ≤ q ≤ 2 ⋅ 10^{5}) — the number of events.

Each of the next q lines contains a single event. The events are given in chronological order.

Each event is described as either 1 p x (1 ≤ p ≤ n, 0 ≤ x ≤ 10^{9}), or 2 x (0 ≤ x ≤ 10^{9}). In the first case we have a receipt that the balance of the p-th person becomes equal to x. In the second case we have a payoff with parameter x.

Output

Print n integers — the balances of all citizens after all events.

Examples

Input


4
1 2 3 4
3
2 3
1 2 2
2 1


Output


3 2 3 4 


Input


5
3 50 2 1 10
3
1 2 0
2 8
1 3 20


Output


8 8 20 8 10 

Note

In the first example the balances change as follows: 1 2 3 4 → 3 3 3 4 → 3 2 3 4 → 3 2 3 4

In the second example the balances change as follows: 3 50 2 1 10 → 3 0 2 1 10 → 8 8 8 8 10 → 8 8 20 8 10
"""

def process_events(n, initial_balances, events):
    # Initialize the final balances list with -1 indicating unprocessed balances
    final_balances = [-1] * n
    # Initialize the maximum payout value seen so far
    max_payout = -1
    
    # Process events in reverse order
    for event in reversed(events):
        t = event[0]
        if t == 1:
            p = event[1] - 1  # Convert to 0-based index
            x = event[2]
            if final_balances[p] == -1:
                final_balances[p] = max(max_payout, x)
        elif t == 2:
            x = event[1]
            max_payout = max(max_payout, x)
    
    # Apply the maximum payout to any unprocessed balances
    for i in range(n):
        if final_balances[i] == -1:
            final_balances[i] = max(initial_balances[i], max_payout)
    
    return final_balances