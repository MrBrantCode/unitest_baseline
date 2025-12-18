"""
QUESTION:
To access CRED programs, one needs to have a credit score of 750 or more.  
Given that the present credit score is X, determine if one can access CRED programs or not.

If it is possible to access CRED programs, output \texttt{YES}, otherwise output \texttt{NO}.

------ Input Format ------ 

The first and only line of input contains a single integer X, the credit score.

------ Output Format ------ 

Print \texttt{YES} if it is possible to access CRED programs. Otherwise, print \texttt{NO}.

You may print each character of the string in uppercase or lowercase (for example, the strings \texttt{YeS}, \texttt{yEs}, \texttt{yes} and \texttt{YES} will all be treated as identical).

------ Constraints ------ 

$0 ≤ X ≤ 1000$

------ subtasks ------ 

Subtask 1 (100 points): Original constraints.

----- Sample Input 1 ------ 
823
----- Sample Output 1 ------ 
YES
----- explanation 1 ------ 
Since $823 ≥ 750$, it is possible to access CRED programs.

----- Sample Input 2 ------ 
251
----- Sample Output 2 ------ 
NO
----- explanation 2 ------ 
Since $251 < 750$, it is not possible to access CRED programs.
"""

def can_access_cred_programs(credit_score: int) -> str:
    if credit_score >= 750:
        return 'YES'
    else:
        return 'NO'