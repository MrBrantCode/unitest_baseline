"""
QUESTION:
After many years of research, Ikta has acquired the ability to predict the future! The time and money he spent on this research was enormous, but it's finally time to be rewarded. To get the money back, Ikta decided to start investing in stocks.

Ikta does not currently own any shares, but owns x yen. He has invested in n stocks, and has succeeded in predicting the stock price for d days from today. As a result, it was surprisingly found that there was no intraday stock price fluctuation for d days from today. In other words, we know the stock price pi, j yen of the stock j (1 ≤ j ≤ n) on the i (1 ≤ i ≤ d) day when today is the first day. Ikta is free to buy and sell stocks each day. That is, the following operations (purchase / sale) can be performed at any time in any order and any number of times. However, the amount of money held and the number of units held of shares before and after each operation must be non-negative integers.

* Purchase: On day i, select one stock type j (1 ≤ j ≤ n) and pay pi, j yen in possession to obtain 1 unit of stock j.
* Sale: On day i, select one stock type j (1 ≤ j ≤ n) and pay 1 unit of stock j to get pi, j yen.



(While he was absorbed in his research, the securities trading system made great progress and there were no transaction fees.)

Ikta had studied information science at university, but had forgotten everything he had learned at university before he could devote himself to future prediction research. Instead of him, write a program that maximizes your money on the final day.



Input

The input is given in the following format.


n d x
p1,1 ... p1, n
...
pd, 1 ... pd, n


* n: Number of stock types
* d: days
* x: Money on the first day
* pi, j: Stock price of stock j on day i (today is the first day)



Constraints

Each variable being input is an integer that satisfies the following constraints.

* 1 ≤ n ≤ 10
* 1 ≤ d ≤ 10
* 1 ≤ x, pi, j ≤ 105
* It is guaranteed that the amount of money you have on the last day will be 105 or less.

Output

Output the last day's money in one line when you invest optimally.

Examples

Input

2 2 5
3 2
5 4


Output

9


Input

1 2 5
6
10000


Output

5


Input

2 3 5
4 5
6 3
8 5


Output

11


Input

3 3 10
10 9 6
8 7 3
7 5 1


Output

10
"""

def maximize_money_on_final_day(n, d, x, stock_prices):
    d -= 1
    price_diff = [[stock_prices[i + 1][j] - stock_prices[i][j] for j in range(n)] for i in range(d)]
    b = x
    
    for i in range(d):
        dp = [False for j in range(b + 1)]
        dp[0] = 0
        for j in range(n):
            for k in range(b):
                if stock_prices[i][j] + k < b + 1 and dp[k] is not False:
                    dp[k + stock_prices[i][j]] = max(dp[k + stock_prices[i][j]], dp[k] + price_diff[i][j])
        b += max(dp[:b + 1])
    
    return b