"""
QUESTION:
Alice has scored X marks in her test and Bob has scored Y marks in the same test. Alice is happy if she scored at least twice the marks of Bob’s score. Determine whether she is happy or not.

------ Input Format ------ 

- The first and only line of input contains two space-separated integers X, Y — the marks of Alice and Bob respectively.

------ Output Format ------ 

For each testcase, print Yes if Alice is happy and No if she is not, according to the problem statement.

The judge is case insensitive so you may output the answer in any case. In particular YES, yes, yEs are all considered equivalent to Yes.

------ Constraints ------ 

$1 ≤ X, Y ≤ 100$

----- Sample Input 1 ------ 
2 1
----- Sample Output 1 ------ 
Yes
----- explanation 1 ------ 
Alice has scored $X = 2$ marks whereas Bob has scored $Y = 1$ mark. As Alice has scored twice as much as Bob (i.e. $X ≥ 2Y$), the answer is Yes.

----- Sample Input 2 ------ 
1 2
----- Sample Output 2 ------ 
No
----- explanation 2 ------ 
Alice has scored $X = 1$ mark whereas Bob has scored $Y = 2$ marks. As Alice has not scored twice as much as Bob (i.e. $X < 2Y$), the answer is No.
"""

def is_alice_happy(x: int, y: int) -> str:
    if x >= 2 * y:
        return 'Yes'
    else:
        return 'No'