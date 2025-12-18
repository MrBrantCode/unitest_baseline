"""
QUESTION:
You are given N items.

The value of the i-th item (1 \leq i \leq N) is v_i.

Your have to select at least A and at most B of these items.

Under this condition, find the maximum possible arithmetic mean of the values of selected items.

Additionally, find the number of ways to select items so that the mean of the values of selected items is maximized.  

-----Constraints-----
 - 1 \leq N \leq 50
 - 1 \leq A,B \leq N
 - 1 \leq v_i \leq 10^{15}
 - Each v_i is an integer.

-----Input-----
The input is given from Standard Input in the following format:
N A B
v_1
v_2
...
v_N

-----Output-----
Print two lines.

The first line should contain the maximum possible arithmetic mean of the values of selected items. The output should be considered correct if the absolute or relative error is at most 10^{-6}.

The second line should contain the number of ways to select items so that the mean of the values of selected items is maximized.

-----Sample Input-----
5 2 2
1 2 3 4 5

-----Sample Output-----
4.500000
1

The mean of the values of selected items will be maximized when selecting the fourth and fifth items. Hence, the first line of the output should contain 4.5.

There is no other way to select items so that the mean of the values will be 4.5, and thus the second line of the output should contain 1.
"""

def max_mean_and_ways(N, A, B, values):
    # Sort the values in descending order
    values.sort(reverse=True)
    
    # Calculate the maximum possible arithmetic mean
    max_mean = sum(values[:A]) / A
    
    # Calculate the number of ways to achieve the maximum mean
    c = values.count(values[A - 1])
    d = values[:A].count(values[A - 1])
    
    def combination(n, r):
        a = 1
        b = 1
        for i in range(1, r + 1):
            a *= n - i + 1
            b *= i
        return a // b
    
    if values[0] != values[A - 1]:
        num_ways = combination(c, d)
    else:
        num_ways = 0
        for i in range(d, min(c, B - A + d) + 1):
            num_ways += combination(c, i)
    
    return max_mean, num_ways