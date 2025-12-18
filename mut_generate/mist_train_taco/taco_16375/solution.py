"""
QUESTION:
Chef is looking to buy a TV and has shortlisted two models. The first one costs A rupees, while the second one costs B rupees.

Since there is a huge sale coming up on Chefzon, Chef can get a flat discount of C rupees on the first TV, and a flat discount of D rupees on the second one.

Help Chef determine which of the two TVs would be cheaper to buy during the sale.

------ Input Format ------ 

- The first line contains a single integer T — the number of test cases. Then the test cases follow.
- The first and only line of each test case contains four space-separated integers A, B, C and D — the marked price (in rupees) of the first TV, the marked price (in rupees) of the second TV, the flat discount (in rupees) of the first TV, and the flat discount (in rupees) of the second TV.

------ Output Format ------ 

For each test case, print a single line containing the string First if the first TV is cheaper to buy with discount, or Second if the second TV is cheaper to buy with discount. If both of them cost the same after discount, print Any.

You may print each character of the string in uppercase or lowercase (for example, the strings first, First, fIRSt, and FIRST will all be treated as identical).

------ Constraints ------ 

$1 ≤ T ≤ 5000$
$1 ≤ A, B ≤ 100$
$0 ≤ C ≤ A$
$0 ≤ D ≤ B$

----- Sample Input 1 ------ 
3
85 75 35 20
100 99 0 0
30 40 0 10

----- Sample Output 1 ------ 
First
Second
Any

----- explanation 1 ------ 
Test case $1$: The cost of the first TV after discount is $85 - 35 = 50$, while the cost of the second TV after discount is $75 - 20 = 55$. Thus the first TV is cheaper to buy than the second.

Test case $2$: The cost of the first TV after discount is $100 - 0 = 100$, while the cost of the second TV after discount is $99 - 0 = 99$. Thus the second TV is cheaper to buy than the first.

Test case $3$: The cost of the first TV after discount is $30 - 0 = 30$, while the cost of the second TV after discount is $40 - 10 = 30$. Since they are equal, Chef can buy any of them.
"""

def compare_tv_prices(A, B, C, D):
    """
    Determines which TV is cheaper to buy after applying the discounts.

    Parameters:
    - A (int): Marked price of the first TV.
    - B (int): Marked price of the second TV.
    - C (int): Flat discount on the first TV.
    - D (int): Flat discount on the second TV.

    Returns:
    - str: A string indicating which TV is cheaper or if both are equally priced.
           Possible values: "First", "Second", or "Any".
    """
    x = A - C
    y = B - D
    
    if x < y:
        return 'First'
    elif x > y:
        return 'Second'
    else:
        return 'Any'