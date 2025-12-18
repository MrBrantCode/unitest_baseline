"""
QUESTION:
It's the sale season again and Chef bought items worth a total of X rupees. The sale season offer is as follows: 
if X ≤ 100, no discount.
if 100 < X ≤ 1000, discount is 25 rupees.
if 1000 < X ≤ 5000, discount is 100 rupees.
if X > 5000, discount is 500 rupees.

Find the final amount Chef needs to pay for his shopping.

------ Input Format ------ 

- The first line of input will contain a single integer T, denoting the number of test cases.
- Each test case consists of single line of input containing an integer X.

------ Output Format ------ 

For each test case, output on a new line the final amount Chef needs to pay for his shopping.

------ Constraints ------ 

$1 ≤ T ≤ 100$
$1 ≤ X ≤ 10000$

----- Sample Input 1 ------ 
4
15
70
250
1000

----- Sample Output 1 ------ 
15
70
225
975

----- explanation 1 ------ 
Test case $1$: Since $X ≤ 100 $, there is no discount.

Test case $3$: Here, $X = 250$. Since $100 < 250 ≤ 1000$, discount is of $25$ rupees. Therefore, Chef needs to pay $250-25 = 225$ rupees.
"""

def calculate_final_amount(X: int) -> int:
    if X <= 100:
        return X
    elif 100 < X <= 1000:
        return X - 25
    elif 1000 < X <= 5000:
        return X - 100
    else:
        return X - 500