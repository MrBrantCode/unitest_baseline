"""
QUESTION:
The employees of the R1 company often spend time together: they watch football, they go camping, they solve contests. So, it's no big deal that sometimes someone pays for someone else.

Today is the day of giving out money rewards. The R1 company CEO will invite employees into his office one by one, rewarding each one for the hard work this month. The CEO knows who owes money to whom. And he also understands that if he invites person x to his office for a reward, and then immediately invite person y, who has lent some money to person x, then they can meet. Of course, in such a situation, the joy of person x from his brand new money reward will be much less. Therefore, the R1 CEO decided to invite the staff in such an order that the described situation will not happen for any pair of employees invited one after another.

However, there are a lot of employees in the company, and the CEO doesn't have a lot of time. Therefore, the task has been assigned to you. Given the debt relationships between all the employees, determine in which order they should be invited to the office of the R1 company CEO, or determine that the described order does not exist.


-----Input-----

The first line contains space-separated integers n and m $(2 \leq n \leq 3 \cdot 10^{4} ; 1 \leq m \leq \operatorname{min}(10^{5}, \frac{n(n - 1)}{2}))$ — the number of employees in R1 and the number of debt relations. Each of the following m lines contains two space-separated integers a_{i}, b_{i} (1 ≤ a_{i}, b_{i} ≤ n; a_{i} ≠ b_{i}), these integers indicate that the person number a_{i} owes money to a person a number b_{i}. Assume that all the employees are numbered from 1 to n.

It is guaranteed that each pair of people p, q is mentioned in the input data at most once. In particular, the input data will not contain pairs p, q and q, p simultaneously.


-----Output-----

Print -1 if the described order does not exist. Otherwise, print the permutation of n distinct integers. The first number should denote the number of the person who goes to the CEO office first, the second number denote the person who goes second and so on.

If there are multiple correct orders, you are allowed to print any of them.


-----Examples-----
Input
2 1
1 2

Output
2 1 

Input
3 3
1 2
2 3
3 1

Output
2 1 3
"""

def determine_invitation_order(n, m, debts):
    # Create a dictionary to store the debt relationships
    P = {(a - 1, b - 1): 1 for a, b in debts}
    
    # Initialize the order list with -1
    A = [-1] * n
    A[0] = 0
    
    # Fill the order list
    for i in range(1, n):
        A[i] = i
        x = i
        while x > 0 and (A[x - 1], A[x]) in P:
            A[x - 1], A[x] = A[x], A[x - 1]
            x -= 1
    
    # Check if the order is valid
    for i in range(1, n):
        if (A[i - 1], A[i]) in P:
            return -1
    
    # Convert the order list to the correct format (1-indexed)
    return [x + 1 for x in A]