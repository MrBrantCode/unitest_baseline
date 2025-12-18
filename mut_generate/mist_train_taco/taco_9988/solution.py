"""
QUESTION:
Alice buys a toy with a selling price of 100 rupees. There is a discount of x percent on the toy. Find the amount Alice needs to pay for it.

------ Input Format ------ 

- The first line of input will contain a single integer T, denoting the number of test cases.
- The first and only line of each test case contains a single integer, x — the discount on the toy.
    
------ Output Format ------ 

For each test case, output on a new line the price that Alice needs to pay.

------ Constraints ------ 

$1 ≤ T ≤ 100$
$0 ≤ x < 100$

----- Sample Input 1 ------ 
4
5
9
11
21

----- Sample Output 1 ------ 
95
91
89
79

----- explanation 1 ------ 
Test case $1$: The discount is $5$ percent, i.e. $5$ rupees. So, Alice will have to pay $100-5=95$ rupees.
"""

def calculate_discounted_price(T, discounts):
    final_prices = []
    for x in discounts:
        final_price = 100 - x
        final_prices.append(final_price)
    return final_prices