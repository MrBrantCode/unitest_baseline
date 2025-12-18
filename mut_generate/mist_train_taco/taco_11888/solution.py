"""
QUESTION:
Chef is planning to buy a new car for his birthday. After a long search, he is left with 2 choices:

Car 1: Runs on diesel with a fuel economy of x_{1} km/l
Car 2: Runs on petrol with a fuel economy of x_{2} km/l

Chef also knows that
the current price of diesel is y_{1} rupees per litre
the current price of petrol is y_{2} rupees per litre

Assuming that both cars cost the same and that the price of fuel remains constant, which car will minimize Chef's expenses?

Print your answer as a single integer in the following format

If it is better to choose Car 1, print -1
If both the cars will result in the same expenses, print 0
If it is better to choose Car 2, print 1

------ Input Format ------ 

- The first line of input contains a single integer T, denoting the number of test cases. The description of T test cases follows.
- Each test case consists of a single line containing 4 space-separated integers — x_{1}, x_{2}, y_{1}, y_{2}.

------ Output Format ------ 

For each test case, output in a single line the answer as explained earlier.

------ Constraints ------ 

$1 ≤ T ≤ 10000$
$1 ≤ x_{1},x_{2},y_{1},y_{2} ≤ 50$

----- Sample Input 1 ------ 
3
10 5 3 20
7 2 7 2
1 5 3 2
----- Sample Output 1 ------ 
-1
0
1
----- explanation 1 ------ 
Test Case $1$: The cost of driving Car 1 is $\frac{3}{10} = 0.3$ rs/km, and the cost of driving Car 2 is $\frac{20}{5} = 4$ rs/km. Therefore, Car 1 is cheaper to drive, so the output is $-1$.

Test Case $2$: The cost of driving Car 1 is $1$ rs/km, and the cost of driving Car 2 is also $1$ rs/km. Both cars offer the same economy, so the output is $0$.

Test Case $3$: The cost of driving Car 1 is $3$ rs/km and the cost of driving Car 2 is $0.4$ rs/km. Therefore, Car 2 is cheaper to drive, so the output is $1$.
"""

def compare_car_expenses(x1: int, x2: int, y1: int, y2: int) -> int:
    """
    Compares the expenses of two cars based on their fuel economy and fuel prices.

    Parameters:
    - x1: Fuel economy of Car 1 in km/l (integer)
    - x2: Fuel economy of Car 2 in km/l (integer)
    - y1: Price of diesel per litre in rupees (integer)
    - y2: Price of petrol per litre in rupees (integer)

    Returns:
    - An integer indicating the result:
      - -1 if Car 1 is cheaper
      - 0 if both cars have the same expense
      - 1 if Car 2 is cheaper
    """
    cost_per_km_car1 = y1 / x1
    cost_per_km_car2 = y2 / x2
    
    if cost_per_km_car1 < cost_per_km_car2:
        return -1
    elif cost_per_km_car1 == cost_per_km_car2:
        return 0
    else:
        return 1