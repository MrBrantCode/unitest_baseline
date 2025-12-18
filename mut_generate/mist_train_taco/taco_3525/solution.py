"""
QUESTION:
Sereja owns a restaurant for n people. The restaurant hall has a coat rack with n hooks. Each restaurant visitor can use a hook to hang his clothes on it. Using the i-th hook costs a_{i} rubles. Only one person can hang clothes on one hook.

Tonight Sereja expects m guests in the restaurant. Naturally, each guest wants to hang his clothes on an available hook with minimum price (if there are multiple such hooks, he chooses any of them). However if the moment a guest arrives the rack has no available hooks, Sereja must pay a d ruble fine to the guest. 

Help Sereja find out the profit in rubles (possibly negative) that he will get tonight. You can assume that before the guests arrive, all hooks on the rack are available, all guests come at different time, nobody besides the m guests is visiting Sereja's restaurant tonight.


-----Input-----

The first line contains two integers n and d (1 ≤ n, d ≤ 100). The next line contains integers a_1, a_2, ..., a_{n} (1 ≤ a_{i} ≤ 100). The third line contains integer m (1 ≤ m ≤ 100).


-----Output-----

In a single line print a single integer — the answer to the problem.


-----Examples-----
Input
2 1
2 1
2

Output
3

Input
2 1
2 1
10

Output
-5



-----Note-----

In the first test both hooks will be used, so Sereja gets 1 + 2 = 3 rubles.

In the second test both hooks will be used but Sereja pays a fine 8 times, so the answer is 3 - 8 =  - 5.
"""

def calculate_profit(n, d, a, m):
    """
    Calculate the profit (possibly negative) that Sereja will get tonight based on the number of hooks,
    the cost to use each hook, the number of guests, and the fine for unavailable hooks.

    Parameters:
    n (int): The number of hooks available in the restaurant.
    d (int): The fine in rubles that Sereja must pay if a guest arrives and there are no available hooks.
    a (list[int]): A list of integers representing the cost in rubles to use each hook.
    m (int): The number of guests expected tonight.

    Returns:
    int: The profit (possibly negative) that Sereja will get tonight.
    """
    a.sort()
    if m <= n:
        profit = sum(a[:m])
    else:
        profit = sum(a) - (m - n) * d
    return profit