"""
QUESTION:
Give me Chocolate

Anushka wants to buy chocolates.there are many chocolates in front of her, tagged with their prices.

Anushka has only a certain amount to spend, and she wants to maximize the number of chocolates she buys with this money.

Given a list of prices and an amount to spend, what is the maximum number of chocolates Anushka can buy? 

For example, 

if prices =[1,2,3,4]
and Anushka has k=7 to spend, she can buy items [1,2,3] for 6 , or [3,4] for 7 units of currency. she would choose the first group of 3 items.

Input Format

The first line contains two integers, n and k , the number of priced chocolates and the amount Anushka has to spend.

The next line contains n space-separated integers prices[i]

Constraints

1<= n <= 105

1<= k <= 109

1<= prices[i] <= 109



A chocolate can't be bought multiple times.

Output Format

An integer that denotes the maximum number of chocolates Anushka can buy for her.

Sample Input

7 50

1 12 5 111 200 1000 10

Sample Output

4

Explanation

she can buy only 4 chocolatess at most. These chocolates have the following prices: 1, 12, 5, 10.
"""

def max_chocolates(prices, k):
    # Sort the prices in ascending order
    prices.sort()
    
    # Initialize variables to keep track of the sum of prices and the count of chocolates
    total_sum = 0
    count = 0
    
    # Iterate through the sorted prices
    for price in prices:
        total_sum += price
        if total_sum <= k:
            count += 1
        else:
            break
    
    # Return the maximum number of chocolates Anushka can buy
    return count