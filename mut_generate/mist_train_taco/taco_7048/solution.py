"""
QUESTION:
A New Year party is not a New Year party without lemonade! As usual, you are expecting a lot of guests, and buying lemonade has already become a pleasant necessity.

Your favorite store sells lemonade in bottles of n different volumes at different costs. A single bottle of type i has volume 2^{i} - 1 liters and costs c_{i} roubles. The number of bottles of each type in the store can be considered infinite.

You want to buy at least L liters of lemonade. How many roubles do you have to spend?


-----Input-----

The first line contains two integers n and L (1 ≤ n ≤ 30; 1 ≤ L ≤ 10^9) — the number of types of bottles in the store and the required amount of lemonade in liters, respectively.

The second line contains n integers c_1, c_2, ..., c_{n} (1 ≤ c_{i} ≤ 10^9) — the costs of bottles of different types.


-----Output-----

Output a single integer — the smallest number of roubles you have to pay in order to buy at least L liters of lemonade.


-----Examples-----
Input
4 12
20 30 70 90

Output
150

Input
4 3
10000 1000 100 10

Output
10

Input
4 3
10 100 1000 10000

Output
30

Input
5 787787787
123456789 234567890 345678901 456789012 987654321

Output
44981600785557577



-----Note-----

In the first example you should buy one 8-liter bottle for 90 roubles and two 2-liter bottles for 30 roubles each. In total you'll get 12 liters of lemonade for just 150 roubles.

In the second example, even though you need only 3 liters, it's cheaper to buy a single 8-liter bottle for 10 roubles.

In the third example it's best to buy three 1-liter bottles for 10 roubles each, getting three liters for 30 roubles.
"""

def calculate_minimum_cost(n, L, costs):
    # Ensure the costs list is long enough to cover all necessary volumes
    for x in range(1, max(n, len(bin(L)) - 2) + 10):
        if x < n:
            if costs[x] > costs[x - 1] * 2:
                costs[x] = costs[x - 1] * 2
        else:
            costs.append(costs[x - 1] * 2)
    
    # Ensure costs are non-increasing
    for x in reversed(range(0, len(costs) - 1)):
        costs[x] = min(costs[x + 1], costs[x])
    
    # Convert L to binary and reverse it
    L_binary = list(reversed(bin(L)))
    
    # Calculate the minimum cost
    ans = 0
    for x in range(max(len(costs), len(L_binary) - 2)):
        if x >= len(L_binary) - 2:
            ans = min(ans, costs[x])
        elif L_binary[x] == '1':
            ans += costs[x]
        else:
            ans = min(ans, costs[x])
    
    return ans