"""
QUESTION:
Given three positive integers X, Y and P. Here P denotes the number of turns. Whenever the turn is odd X is multiplied by 2 and in every even turn Y is multiplied by 2.Find the value of Max(X, Y) ÷ Min(X, Y) after the completion of P turns.
Example 1:
Input:
X=1
Y=2
P=1
Output:
1
Explanation:
After 1st turn,
X=2,Y=2.
Now Max(X,Y)/Min(X,Y)=1.
Example 2:
Input:
X=2
Y=1
P=2
Output:
2
Explanation:
After first turn,
X=4,Y=1
After Second turn,
X=4,Y=2.
Now,Max(X,Y)/Min(X,Y)=4/2=2.
Your Task:
You don't need to read input or print anything.Your task is to complete the function findValue() which takes 3 integers X,Y,P as input parameters and returns the value of Max(X,Y)/Min(X,Y) after P turns.
Expected Time Complexity:O(1)
Expected Auxillary Space:O(1)
Constraints:
1<=X,Y,P<=10^{9}
"""

def calculate_max_min_ratio(X: int, Y: int, P: int) -> int:
    if P % 2 == 0:
        return int(max(X, Y) / min(X, Y))
    else:
        return int(max(2 * X, Y) / min(2 * X, Y))