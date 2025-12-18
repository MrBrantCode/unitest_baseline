"""
QUESTION:
There are 2 stores in Chefland and both sell the same product. The first store sells the product for 100 rupees whereas the second store sells it for 200 rupees.

It is the holiday season and both stores have announced a special discount. The first store is providing a discount of A percent on its product and the second store is providing a discount of B percent on its product.

Chef is wondering which store is selling the product at a cheaper price after the discount has been applied. Can you help him identify the better deal?

------ Input Format ------ 

- The first line of input will contain a single integer T, denoting the number of test cases.
- Each test case consists of a single line of input containing two space-separated integers A and B denoting the discount provided by the first and second store respectively. 

------ Output Format ------ 

For each test case, output FIRST if the first store is cheaper, SECOND if the second store is cheaper, and BOTH if both the stores are selling the product for the same price after discount.

The checker is case-insensitive so answers like FiRsT, first, and FIRST would be considered the same.

------ Constraints ------ 

$1 ≤ T ≤ 1000$
$1 ≤ A, B ≤ 100$

----- Sample Input 1 ------ 
4
5 20
10 60
7 7
10 55

----- Sample Output 1 ------ 
FIRST
SECOND
FIRST
BOTH

----- explanation 1 ------ 
Test case $1$: The first store has a discount of $5\%$. Thus, the final price of product at first store would be $95$.  
The second store has a discount of $20\%$. Thus, the final price of the product at the second store would be $160$. The product at the first store would be cheaper.

Test case $2$: The first store has a discount of $10\%$. Thus, the final price of product at first store would be $90$.  
The second store has a discount of $60\%$. Thus, the final price of the product at the second store would be $80$. The product at the second store would be cheaper.

Test case $3$: The first store has a discount of $7\%$. Thus, the final price of product at first store would be $93$.  
The second store has a discount of $7\%$. Thus, the final price of the product at the second store would be $186$. The product at the first store would be cheaper.

Test case $4$: The first store has a discount of $10\%$. Thus, the final price of product at first store would be $90$.  
The second store has a discount of $55\%$. Thus, the final price of the product at the second store would be $90$. The product at both stores would have same price.
"""

def compare_store_prices(A: int, B: int) -> str:
    # Calculate the final price after discount for both stores
    price_first_store = 100 - (A * 100 / 100)
    price_second_store = 200 - (B * 200 / 100)
    
    # Compare the prices and return the appropriate result
    if price_first_store == price_second_store:
        return "BOTH"
    elif price_first_store < price_second_store:
        return "FIRST"
    else:
        return "SECOND"