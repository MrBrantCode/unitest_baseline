"""
QUESTION:
*Chef has recently introduced a [feature] which allows you to open any user’s submitted code (not just your own), and ask an AI to explain that code in English. For example, you can go to https://www.codechef.com/viewsolution/70530506 and click on "Analyse This Code".*

But there is a restriction that the feature works only on codes which are at most 1000 characters long. Given the number of characters, C, in a particular code, output whether the feature is available on this code or not.

------ Input Format ------ 

The only line of input will contain a single integer C, denoting the number of characters in the code.

------ Output Format ------ 

Output a single line which contains either "Yes", if the feature is available on this code, or "No", if not.

You may print each character of the string in either uppercase or lowercase (for example, the strings NO, nO, No, and no will all be treated as identical).

------ Constraints ------ 

$1 ≤ C ≤ 10000$

----- Sample Input 1 ------ 
50

----- Sample Output 1 ------ 
Yes
----- explanation 1 ------ 
The code's length is only $50$, and $50 ≤ 1000$. So, the feature is available, and the answer is "Yes".

----- Sample Input 2 ------ 
1000

----- Sample Output 2 ------ 
Yes
----- explanation 2 ------ 
The code's length is $1000$, and $1000 ≤ 1000$. So, the feature is available, and the answer is "Yes".

----- Sample Input 3 ------ 
1001

----- Sample Output 3 ------ 
No
----- explanation 3 ------ 
The code's length is $1001$, and $1001 \nleq 1000$. So, the feature is not available, and the answer is "No".
"""

def is_feature_available(C: int) -> str:
    if C <= 1000:
        return 'Yes'
    else:
        return 'No'