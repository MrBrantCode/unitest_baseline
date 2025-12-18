"""
QUESTION:
There are n lights aligned in a row. These lights are numbered 1 to n from left to right. Initially some of the lights are switched on. Shaass wants to switch all the lights on. At each step he can switch a light on (this light should be switched off at that moment) if there's at least one adjacent light which is already switched on. 

He knows the initial state of lights and he's wondering how many different ways there exist to switch all the lights on. Please find the required number of ways modulo 1000000007 (10^9 + 7).


-----Input-----

The first line of the input contains two integers n and m where n is the number of lights in the sequence and m is the number of lights which are initially switched on, (1 ≤ n ≤ 1000, 1 ≤ m ≤ n). The second line contains m distinct integers, each between 1 to n inclusive, denoting the indices of lights which are initially switched on.


-----Output-----

In the only line of the output print the number of different possible ways to switch on all the lights modulo 1000000007 (10^9 + 7).


-----Examples-----
Input
3 1
1

Output
1

Input
4 2
1 4

Output
2

Input
11 2
4 8

Output
6720
"""

from math import factorial

def count_ways_to_switch_lights(n, m, lights):
    MOD = 10**9 + 7
    
    # Sort the initial lights and add boundary conditions
    lights.sort()
    lights = [0] + lights + [n + 1]
    
    # Calculate the gaps between the lights
    x = [lights[i + 1] - lights[i] - 1 for i in range(len(lights) - 1)]
    
    # Calculate the total number of gaps
    s = sum(x)
    
    # Initialize the product with the factorial of the total gaps
    prod = factorial(s)
    
    # Divide by the factorial of each gap
    for i in x:
        prod //= factorial(i)
    
    # If there are more than 2 gaps, adjust for the internal gaps
    if len(x) >= 3:
        for i in range(1, len(x) - 1):
            if x[i] > 0:
                prod *= pow(2, x[i] - 1, MOD)
    
    # Return the result modulo 10^9 + 7
    return prod % MOD