"""
QUESTION:
Chef made two laddus with sweetness X and Y respectively. Cheffina comes and sees the chef created two laddus with different sweetness (might be same). Cheffina has the magical power to make the sweetness of laddus equal. Cheffina requires 1 unit of power to increase the sweetness of laddu by its original value i.e. 1 unit to convert Z to 2Z and 2 unit to convert Z to 3Z and so on… How many units of power does cheffina want to make the sweetness equal?

-----Input:-----
- First-line will contain $T$, the number of test cases. Then the test cases follow. 
- Each test case contains a single line of input, two integers $X, Y$. 

-----Output:-----
For each test case, output in a single line answer as power required.

-----Constraints-----
- $1 \leq T \leq 10^5$
- $1 \leq X,Y \leq 10^5$

-----Sample Input:-----
2
2 2
4 6

-----Sample Output:-----
0
3

-----EXPLANATION:-----
For 1) Sweetness are same so no need to use power.
For 2) 
1st laddu
2 Unit power = 4 -> 12
2nd Laddu
1 Unit power = 6 -> 12
After using total 3 unit power sweetness of both laddus are same.
"""

def calculate_power_to_equalize_sweetness(test_cases):
    def gcd(a, b):
        if b == 0:
            return a
        else:
            return gcd(b, a % b)

    def lcm(a, b):
        m = a * b
        g = gcd(a, b)
        return int(m / g)

    results = []
    for x, y in test_cases:
        l = lcm(x, y)
        s = int(l / x)
        t = int(l / y)
        results.append(s + t - 2)
    
    return results