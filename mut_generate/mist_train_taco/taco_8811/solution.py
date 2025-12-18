"""
QUESTION:
Chef is the financial incharge of Chefland and one of his duties is identifying if any company has gained a monopolistic advantage in the market.

There are exactly 3 companies in the market each of whose revenues are denoted by R_{1}, R_{2} and R_{3} respectively. A company is said to have a monopolistic advantage if its revenue is strictly greater than the sum of the revenues of its competitors.

Given the revenue of the 3 companies, help Chef determine if any of them has a monopolistic advantage.

------ Input Format ------ 

- The first line of input will contain a single integer T, denoting the number of test cases.
- Each test case consists of a single line of input containing three space separated integers R_{1}, R_{2} and R_{3} denoting the revenue of the three companies respectively.

------ Output Format ------ 

For each test case, output \texttt{YES} if any of the companies has a monopolistic advantage over its competitors, else output \texttt{NO}. 

You may print each character of the string in uppercase or lowercase (for example, the strings \texttt{YeS}, \texttt{yEs}, \texttt{yes} and \texttt{YES} will all be treated as identical).

------ Constraints ------ 

$1 ≤ T ≤ 1000$
$1 ≤ R_{1}, R_{2}, R_{3} ≤ 10$

----- Sample Input 1 ------ 
4
1 1 1
1 2 4
2 10 3
1 2 3

----- Sample Output 1 ------ 
No
Yes
Yes
No

----- explanation 1 ------ 
Test case 1: All the companies have equal revenue so none have a monopolistic advantage.

Test case 2: The third company has a monopolistic advantage as $1 + 2 < 4$.

Test case 3: The second company has a monopolistic advantage as $2 + 3 < 10$.
"""

def has_monopolistic_advantage(revenues):
    # Unpack the revenues
    r1, r2, r3 = revenues
    
    # Check if any company has a monopolistic advantage
    if r1 > r2 + r3 or r2 > r1 + r3 or r3 > r1 + r2:
        return "YES"
    else:
        return "NO"