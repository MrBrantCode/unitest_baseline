"""
QUESTION:
All cities of Lineland are located on the Ox coordinate axis. Thus, each city is associated with its position x_{i} — a coordinate on the Ox axis. No two cities are located at a single point.

Lineland residents love to send letters to each other. A person may send a letter only if the recipient lives in another city (because if they live in the same city, then it is easier to drop in).

Strange but true, the cost of sending the letter is exactly equal to the distance between the sender's city and the recipient's city.

For each city calculate two values ​​min_{i} and max_{i}, where min_{i} is the minimum cost of sending a letter from the i-th city to some other city, and max_{i} is the the maximum cost of sending a letter from the i-th city to some other city


-----Input-----

The first line of the input contains integer n (2 ≤ n ≤ 10^5) — the number of cities in Lineland. The second line contains the sequence of n distinct integers x_1, x_2, ..., x_{n} ( - 10^9 ≤ x_{i} ≤ 10^9), where x_{i} is the x-coordinate of the i-th city. All the x_{i}'s are distinct and follow in ascending order.


-----Output-----

Print n lines, the i-th line must contain two integers min_{i}, max_{i}, separated by a space, where min_{i} is the minimum cost of sending a letter from the i-th city, and max_{i} is the maximum cost of sending a letter from the i-th city.


-----Examples-----
Input
4
-5 -2 2 7

Output
3 12
3 9
4 7
5 12

Input
2
-1 1

Output
2 2
2 2
"""

def calculate_min_max_costs(n, coordinates):
    results = []
    for i in range(n):
        if i == 0:
            min_cost = abs(coordinates[0] - coordinates[1])
            max_cost = abs(coordinates[0] - coordinates[n - 1])
        elif i == n - 1:
            min_cost = abs(coordinates[n - 1] - coordinates[n - 2])
            max_cost = abs(coordinates[n - 1] - coordinates[0])
        else:
            min_cost = min(abs(coordinates[i] - coordinates[i - 1]), abs(coordinates[i] - coordinates[i + 1]))
            max_cost = max(abs(coordinates[i] - coordinates[0]), abs(coordinates[i] - coordinates[n - 1]))
        
        results.append((min_cost, max_cost))
    
    return results