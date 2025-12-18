"""
QUESTION:
Chef has invested his money at an interest rate of X percent per annum while the current inflation rate is Y percent per annum. 

An investment is called *good* if and only if the interest rate of the investment is at least twice of the inflation rate.  
Determine whether the investment made by Chef is *good* or not.

------ Input Format ------ 

- The first line of input will contain a single integer T, denoting the number of test cases.
- Each test case consists of two integers X and Y, the interest rate and the current inflation rate respectively.

------ Output Format ------ 

For each test case, output YES if the investment is good, NO otherwise.

You can output any letter in any case. For example YES, yes, yES are all considered same.

------ Constraints ------ 

$1 ≤ T ≤ 400$
$1 ≤ X, Y ≤ 20$

----- Sample Input 1 ------ 
5
7 4
6 3
2 4
10 10
20 1

----- Sample Output 1 ------ 
NO
YES
NO
NO
YES

----- explanation 1 ------ 
Test case $1$: The interest rate is $7$ and the current inflation rate is $4$. Since the interest rate is less than twice of current inflation rate, the investment is not good.

Test case $2$: The interest rate is $6$ and the current inflation rate is $3$. Since the interest rate is equal to twice of current inflation rate, the investment is good.

Test case $3$: The interest rate is $2$ and the current inflation rate is $4$. Since the interest rate is less than twice of current inflation rate, the investment is not good.

Test case $4$: The interest rate is $10$ and the current inflation rate is $10$. Since the interest rate is less than twice of current inflation rate, the investment is not good.

Test case $5$: The interest rate is $20$ and the current inflation rate is $1$. Since the interest rate is greater than twice of current inflation rate, the investment is good.
"""

def is_investment_good(interest_rate: int, inflation_rate: int) -> str:
    """
    Determines whether an investment is good based on the interest rate and inflation rate.

    An investment is considered good if the interest rate is at least twice the inflation rate.

    Parameters:
    - interest_rate (int): The interest rate of the investment.
    - inflation_rate (int): The current inflation rate.

    Returns:
    - str: "YES" if the investment is good, "NO" otherwise.
    """
    if interest_rate >= 2 * inflation_rate:
        return "YES"
    else:
        return "NO"