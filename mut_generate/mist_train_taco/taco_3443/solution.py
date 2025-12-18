"""
QUESTION:
In a long narrow forest stretching east-west, there are N beasts. Below, we will call the point that is p meters from the west end Point p. The i-th beast from the west (1 ≤ i ≤ N) is at Point x_i, and can be sold for s_i yen (the currency of Japan) if captured.

You will choose two integers L and R (L ≤ R), and throw a net to cover the range from Point L to Point R including both ends, [L, R]. Then, all the beasts in the range will be captured. However, the net costs R - L yen and your profit will be (the sum of s_i over all captured beasts i) - (R - L) yen.

What is the maximum profit that can be earned by throwing a net only once?

Constraints

* 1 ≤ N ≤ 2 × 10^5
* 1 ≤ x_1 < x_2 < ... < x_N ≤ 10^{15}
* 1 ≤ s_i ≤ 10^9
* All input values are integers.

Input

Input is given from Standard Input in the following format:


N
x_1 s_1
x_2 s_2
:
x_N s_N


Output

When the maximum profit is X yen, print the value of X.

Examples

Input

5
10 20
40 50
60 30
70 40
90 10


Output

90


Input

5
10 2
40 5
60 3
70 4
90 1


Output

5


Input

4
1 100
3 200
999999999999999 150
1000000000000000 150


Output

299
"""

def max_profit_in_forest(N, beasts):
    ans = 0
    tmp = 0
    prev = 0
    
    for x, s in beasts:
        dx = x - prev
        if dx > tmp:
            tmp = s
        else:
            tmp += s - dx
        ans = max(ans, tmp)
        prev = x
    
    return max(ans, tmp)