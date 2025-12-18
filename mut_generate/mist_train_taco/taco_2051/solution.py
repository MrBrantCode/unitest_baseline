"""
QUESTION:
There are $n$ people at the railway station, and each one wants to buy a ticket to go to one of $\boldsymbol{\mbox{k}}$ different destinations. The $n$ people are in a queue.  

There are $m$ ticket windows from which tickets can be purchased. The $n$ people will be distributed in the windows such that the order is maintained. In other words, suppose we number the people $1$ to $n$ from front to back. If person $\boldsymbol{i}$ and person $j$ go to the same window and $i<j$, then person $\boldsymbol{i}$ should still be ahead of person $j$ in the window.  

Each ticketing window has an offer. If a person in the queue shares the same destination as the person immediately in front of him/her, a 20% reduction in the ticket price is offered to him/her.  

For example, suppose there are $3$ people in the queue for a single ticket window, all with the same destination which costs $10$ bucks. Then the first person in the queue pays $10$ bucks, and the 2nd and 3rd persons get a discount of 20% on $10$ bucks, so they end up paying $8$ bucks each instead of $10$ bucks.  

Try to distribute the $n$ people across the $m$ windows such that the total cost $\mbox{S}$ paid by all $n$ people is minimized.  

Input Format

The first line contains $3$ integers:

$n$ is the number of people  
$m$ is the number of ticket windows  
$\boldsymbol{\mbox{k}}$ is the number of destinations separated by a single space (in the same order) 

Then $\boldsymbol{\mbox{k}}$ lines follow. The $i^{\cdot t h}$ line contains an alphanumeric string $\textbf{place}_i$ and an integer $\textbf{price}_i$:

$\textbf{place}_i$ is the $i^{\cdot t h}$ destination  
$\textbf{price}_i$ is the ticket price for $\textbf{place}_i$  

Then $n$ lines follow. The $i^{\cdot t h}$ line contains an alphanumeric string $\textbf{destination}_i$ which is the destination of the $i^{\cdot t h}$ person.  

Constraints

$1\leq n\leq500$  
$1\leq m\leq10$  
$1\leq k\leq100$  
The $\boldsymbol{\mbox{k}}$ available destinations have nonempty and distinct names.  
Each person's destination appears in the list of $\boldsymbol{\mbox{k}}$ available destinations.  
$0\leq\text{price}_i\leq100$  

Output Format

Output $n+1$ lines. The first line contains $\mbox{S}$, the total cost that is to be minimized. In the $i^{\cdot t h}$ following line, print the ticket window which the $i^{\cdot t h}$ person goes to. The windows are indexed $1$ to $m$. There may be multiple ways to distribute the people among the windows such that the total cost is minimized; any one will be accepted.  

The answer $\mbox{S}$ will be accepted if it is within an error of $10^{-3}$ of the true answer.  

Sample Input
5 2 3
CALIFORNIA 10
HAWAII 8
NEWYORK 12
NEWYORK
NEWYORK
CALIFORNIA
NEWYORK
HAWAII

Sample Output
49.2
1
1
2
1
1

Explanation

At the beginning, all the people are in the same queue, and will go to the ticket windows one by one in the initial order.  

$\{1,2,4,5\}$ will buy ticket in the first window. 
$\{3\}$ will buy ticket in the second window.  

In the first ticket window, #1 will pay $12$ bucks to go to NEWYORK, and #2 and #4 have the same destination with the person in front of them, so they will get 20% off, and will pay $9.6$ bucks each. #5 has a different destination, so it will cost him $8$ bucks to go to HAWAII.  

In the second ticket window, #3 will pay $10$ bucks to go to CALIFORNIA.
"""

import heapq
import math
from collections import defaultdict, namedtuple

State = namedtuple('State', ['passenger', 'window', 'windows_visible_destinations'])

def minimize_ticket_cost(n, m, k, destinations, people_destinations):
    price = {dest[0]: dest[1] for dest in destinations}
    cost = defaultdict(lambda: math.inf)
    start_state = State(0, 0, tuple([people_destinations[0]] + ['no destination'] * (m - 1)))
    start_state_cost = price[people_destinations[start_state.passenger]]
    parent = {start_state: None}
    cost[start_state.passenger, frozenset(start_state.windows_visible_destinations)] = start_state_cost
    states_pq = [(start_state_cost, start_state)]
    
    while states_pq:
        current_cost, state = heapq.heappop(states_pq)
        if current_cost > cost[state.passenger, frozenset(state.windows_visible_destinations)]:
            continue
        if state.passenger < n - 1:
            for next_price, next_state in next_states(state, people_destinations, price):
                if current_cost + next_price < cost[next_state.passenger, frozenset(next_state.windows_visible_destinations)]:
                    cost[next_state.passenger, frozenset(next_state.windows_visible_destinations)] = current_cost + next_price
                    parent[next_state] = state
                    heapq.heappush(states_pq, (current_cost + next_price, next_state))
        else:
            total_cost = current_cost
            allocation_list = solution_path(state, parent)
            return total_cost, allocation_list

def next_states(state, people_destinations, price):
    result = []
    seen_next_windows_visible_destinations = set()
    next_destination = people_destinations[state.passenger + 1]
    next_price = price[next_destination]
    for i, destination in enumerate(state.windows_visible_destinations):
        if destination == next_destination:
            return [(next_price * 0.8, State(state.passenger + 1, i, state.windows_visible_destinations))]
        else:
            next_windows_visible_destinations = list(state.windows_visible_destinations)
            next_windows_visible_destinations[i] = next_destination
            if frozenset(next_windows_visible_destinations) not in seen_next_windows_visible_destinations:
                seen_next_windows_visible_destinations.add(frozenset(next_windows_visible_destinations))
                result.append((next_price, State(state.passenger + 1, i, tuple(next_windows_visible_destinations))))
    return result

def solution_path(state, parent):
    people_windows = []
    while state:
        people_windows.insert(0, state.window)
        state = parent[state]
    return people_windows