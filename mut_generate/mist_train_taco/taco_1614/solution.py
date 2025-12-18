"""
QUESTION:
Sasha is a very happy guy, that's why he is always on the move. There are $n$ cities in the country where Sasha lives. They are all located on one straight line, and for convenience, they are numbered from $1$ to $n$ in increasing order. The distance between any two adjacent cities is equal to $1$ kilometer. Since all roads in the country are directed, it's possible to reach the city $y$ from the city $x$ only if $x < y$. 

Once Sasha decided to go on a trip around the country and to visit all $n$ cities. He will move with the help of his car, Cheetah-2677. The tank capacity of this model is $v$ liters, and it spends exactly $1$ liter of fuel for $1$ kilometer of the way. At the beginning of the journey, the tank is empty. Sasha is located in the city with the number $1$ and wants to get to the city with the number $n$. There is a gas station in each city. In the $i$-th city, the price of $1$ liter of fuel is $i$ dollars. It is obvious that at any moment of time, the tank can contain at most $v$ liters of fuel.

Sasha doesn't like to waste money, that's why he wants to know what is the minimum amount of money is needed to finish the trip if he can buy fuel in any city he wants. Help him to figure it out!


-----Input-----

The first line contains two integers $n$ and $v$ ($2 \le n \le 100$, $1 \le v \le 100$)  — the number of cities in the country and the capacity of the tank.


-----Output-----

Print one integer — the minimum amount of money that is needed to finish the trip.


-----Examples-----
Input
4 2

Output
4

Input
7 6

Output
6



-----Note-----

In the first example, Sasha can buy $2$ liters for $2$ dollars ($1$ dollar per liter) in the first city, drive to the second city, spend $1$ liter of fuel on it, then buy $1$ liter for $2$ dollars in the second city and then drive to the $4$-th city. Therefore, the answer is $1+1+2=4$.

In the second example, the capacity of the tank allows to fill the tank completely in the first city, and drive to the last city without stops in other cities.
"""

def calculate_minimum_fuel_cost(n, v):
    # Calculate the total distance to be covered
    total_distance = n - 1
    
    # If the tank capacity is greater than or equal to the total distance,
    # Sasha can fill the tank completely in the first city and drive to the last city.
    if total_distance <= v:
        return total_distance
    
    # Otherwise, Sasha needs to buy fuel in multiple cities.
    # The minimum cost is the cost of filling the tank in the first city
    # plus the cost of buying fuel in subsequent cities.
    min_cost = v  # Cost of filling the tank in the first city
    remaining_distance = total_distance - v
    
    # Calculate the cost of buying fuel in subsequent cities
    for i in range(2, remaining_distance + 2):
        min_cost += i
    
    return min_cost