"""
QUESTION:
While playing in the plains, Chef found a point A with coordinates (X, Y). 

Chef is interested in finding the number of [straight lines] passing through the point A such that their [intercepts] on both axes are positive integers. 

------ Input Format ------ 

- First and only line of input contains two integers X and Y - the coordinates of the point A.

------ Output Format ------ 

- For each test case, print an integer - the number of lines satisfying the given conditions.

------ Constraints ------ 

$1 ≤ X ≤ 10^{12}$
$1 ≤ Y ≤ 10^{12}$

----- Sample Input 1 ------ 
3 2
----- Sample Output 1 ------ 
4
----- explanation 1 ------ 
There are $4$ lines satisfying all the conditions. These lines are:

![image]

----- Sample Input 2 ------ 
1 2
----- Sample Output 2 ------ 
2
----- explanation 2 ------ 
There are $2$ such lines, which are :

![image]

----- Sample Input 3 ------ 
28 206
----- Sample Output 3 ------ 
16
----- explanation 3 ------ 
There are $16$ such lines.
"""

import math

def count_positive_intercept_lines(x, y):
    n = x * y
    ans = 1
    
    for i in range(2, int(math.sqrt(n)) + 2):
        if i > math.sqrt(n) + 1:
            break
        if n % i == 0:
            count = 0
            while n % i == 0:
                n = n // i
                count += 1
            ans *= count + 1
    
    if n > 1:
        ans *= 2
    
    return ans