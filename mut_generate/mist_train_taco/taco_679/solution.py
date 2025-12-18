"""
QUESTION:
There is a country with $n$ citizens. The $i$-th of them initially has $a_{i}$ money. The government strictly controls the wealth of its citizens. Whenever a citizen makes a purchase or earns some money, they must send a receipt to the social services mentioning the amount of money they currently have.

Sometimes the government makes payouts to the poor: all citizens who have strictly less money than $x$ are paid accordingly so that after the payout they have exactly $x$ money. In this case the citizens don't send a receipt.

You know the initial wealth of every citizen and the log of all events: receipts and payouts. Restore the amount of money each citizen has after all events.


-----Input-----

The first line contains a single integer $n$ ($1 \le n \le 2 \cdot 10^{5}$) — the numer of citizens.

The next line contains $n$ integers $a_1$, $a_2$, ..., $a_n$ ($0 \le a_{i} \le 10^{9}$) — the initial balances of citizens.

The next line contains a single integer $q$ ($1 \le q \le 2 \cdot 10^{5}$) — the number of events.

Each of the next $q$ lines contains a single event. The events are given in chronological order.

Each event is described as either 1 p x ($1 \le p \le n$, $0 \le x \le 10^{9}$), or 2 x ($0 \le x \le 10^{9}$). In the first case we have a receipt that the balance of the $p$-th person becomes equal to $x$. In the second case we have a payoff with parameter $x$.


-----Output-----

Print $n$ integers — the balances of all citizens after all events.


-----Examples-----
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



-----Note-----

In the first example the balances change as follows: 1 2 3 4 $\rightarrow$ 3 3 3 4 $\rightarrow$ 3 2 3 4 $\rightarrow$ 3 2 3 4

In the second example the balances change as follows: 3 50 2 1 10 $\rightarrow$ 3 0 2 1 10 $\rightarrow$ 8 8 8 8 10 $\rightarrow$ 8 8 20 8 10
"""

def calculate_final_balances(n, initial_balances, events):
    last_updated = [0] * n
    pay_days = [0] * len(events)
    
    for i, event in enumerate(events):
        if event[0] == 1:
            _, p, x = event
            initial_balances[p - 1] = x
            last_updated[p - 1] = i
        else:
            _, x = event
            pay_days[i] = x
    
    for i in range(len(events) - 1):
        pay_days[len(events) - i - 2] = max(pay_days[len(events) - i - 1], pay_days[len(events) - i - 2])
    
    final_balances = [max(initial_balances[i], pay_days[last_updated[i]]) for i in range(n)]
    
    return final_balances