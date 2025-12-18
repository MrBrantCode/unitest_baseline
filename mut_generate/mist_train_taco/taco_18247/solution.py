"""
QUESTION:
Bob has X rupees and goes to a market. The cost of apples is Rs. A per kg and the cost of oranges is Rs. B per kg.

Determine whether he can buy at least 1 kg each of apples and oranges.

------ Input Format ------ 

- The first line of input will contain an integer X, the amount of money Bob has.
- The second line of input contains two space-separated integers A and B, the cost per kg of apples and oranges respectively.

------ Output Format ------ 

Print a single line containing Yes if Bob can buy the fruits and No otherwise.

You may print each character of the string in uppercase or lowercase (for example, the strings yes, Yes, yEs, and YES will all be treated as identical).

------ Constraints ------ 

$1 ≤ X,A,B ≤ 10^{5}$

------ subtasks ------ 

Subtask 1 (100 points):
Original constraints.

----- Sample Input 1 ------ 
14 
2 2
----- Sample Output 1 ------ 
Yes
----- explanation 1 ------ 
The cost of buying $1$ kg each of apple and orange is $2+2 = 4$. Since Bob has more than $4$ rupees, the answer will be Yes.

----- Sample Input 2 ------ 
1 
1 1
----- Sample Output 2 ------ 
No
----- explanation 2 ------ 
Bob can only buy either $1$ kg of apples or $1$ kg of oranges with $1$ rupee, hence the answer is No.

----- Sample Input 3 ------ 
5
3 2

----- Sample Output 3 ------ 
Yes
----- explanation 3 ------ 
The cost of buying $1$ kg each of apple and orange is $3+2 = 5$. Since Bob has exactly $5$ rupees, the answer will be Yes.

----- Sample Input 4 ------ 
10000
5000 6000

----- Sample Output 4 ------ 
No
----- explanation 4 ------ 
The cost of buying $1$ kg each of apple and orange is $5000+6000 = 11000$. Since Bob has only $10000$ rupees, the answer will be No.
"""

def can_buy_fruits(X: int, A: int, B: int) -> str:
    if A + B <= X:
        return 'Yes'
    else:
        return 'No'