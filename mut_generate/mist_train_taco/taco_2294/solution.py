"""
QUESTION:
Johnny drives a truck and must deliver a package from his hometown to the district center. His hometown is located at point 0 on a number line, and the district center is located at the point d.

Johnny's truck has a gas tank that holds exactly n liters, and his tank is initially full. As he drives, the truck consumes exactly one liter per unit distance traveled. Moreover, there are m gas stations located at various points along the way to the district center. The i-th station is located at the point x_{i} on the number line and sells an unlimited amount of fuel at a price of p_{i} dollars per liter. Find the minimum cost Johnny must pay for fuel to successfully complete the delivery.


-----Input-----

The first line of input contains three space separated integers d, n, and m (1 ≤ n ≤ d ≤ 10^9, 1 ≤ m ≤ 200 000) — the total distance to the district center, the volume of the gas tank, and the number of gas stations, respectively.

Each of the next m lines contains two integers x_{i}, p_{i} (1 ≤ x_{i} ≤ d - 1, 1 ≤ p_{i} ≤ 10^6) — the position and cost of gas at the i-th gas station. It is guaranteed that the positions of the gas stations are distinct.


-----Output-----

Print a single integer — the minimum cost to complete the delivery. If there is no way to complete the delivery, print -1.


-----Examples-----
Input
10 4 4
3 5
5 8
6 3
8 4

Output
22

Input
16 5 2
8 2
5 1

Output
-1



-----Note-----

In the first sample, Johnny's truck holds 4 liters. He can drive 3 units to the first gas station, buy 2 liters of gas there (bringing the tank to 3 liters total), drive 3 more units to the third gas station, buy 4 liters there to fill up his tank, and then drive straight to the district center. His total cost is 2·5 + 4·3 = 22 dollars.

In the second sample, there is no way for Johnny to make it to the district center, as his tank cannot hold enough gas to take him from the latest gas station to the district center.
"""

def calculate_minimum_fuel_cost(d, n, m, gas_stations):
    start_point = 0
    gas_prices = {start_point: 0}
    
    for coordinate, price in gas_stations:
        gas_prices[coordinate] = price
    
    points = sorted(gas_prices.keys(), reverse=True)
    current_point = start_point
    count = 0
    gas_tank_volume = n
    reachable_points = []
    
    while current_point != d:
        farthest_reachable_point = current_point + gas_tank_volume
        
        while points and points[-1] <= farthest_reachable_point:
            reachable_points.append(points.pop())
        
        if reachable_points:
            cheaper_reachable_points = sorted(filter(lambda point: gas_prices[point] < gas_prices[current_point], reachable_points))
            next_point = cheaper_reachable_points[0] if cheaper_reachable_points else min(reachable_points, key=lambda point: gas_prices[point])
            
            if farthest_reachable_point >= d and (current_point == start_point or gas_prices[next_point] >= gas_prices[current_point]):
                next_point = d
            else:
                reachable_points = [point for point in reachable_points if point > next_point]
        elif farthest_reachable_point >= d:
            next_point = d
        else:
            return -1
        
        distance = next_point - current_point
        
        if next_point != d and gas_prices[current_point] <= gas_prices[next_point]:
            required_gas_volume = n
        else:
            required_gas_volume = distance
        
        if required_gas_volume > gas_tank_volume:
            count += (required_gas_volume - gas_tank_volume) * gas_prices[current_point]
            gas_tank_volume = required_gas_volume
        
        current_point = next_point
        gas_tank_volume -= distance
    
    return count