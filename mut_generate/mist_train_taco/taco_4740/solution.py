"""
QUESTION:
Alice is a kindergarten teacher. She wants to give some candies to the children in her class.  All the children sit in a line and each of them has a rating score according to his or her performance in the class.  Alice wants to give at least 1 candy to each child. If two children sit next to each other, then the one with the higher rating must get more candies. Alice wants to minimize the total number of candies she must buy.

Example  

$arr=[4,6,4,5,6,2]$    

She gives the students candy in the following minimal amounts: $[1,2,1,2,3,1]$.  She must buy a minimum of 10 candies.  

Function Description

Complete the candies function in the editor below.  

candies has the following parameter(s):  

int n: the number of children in the class  
int arr[n]: the ratings of each student  

Returns  

int: the minimum number of candies Alice must buy  

Input Format

The first line contains an integer, $n$, the size of $\textbf{arr}$. 

Each of the next $n$ lines contains an integer $arr\left[i\right]$ indicating the rating of the student at position $\boldsymbol{i}$.

Constraints

$1\leq n\leq10^5$  
$1\leq ar r[i]\leq10^5$ 

Sample Input 0
3
1
2
2

Sample Output 0
4

Explanation 0

Here 1, 2, 2 is the rating. Note that when two children have equal rating, they are allowed to have different number of candies. Hence optimal distribution will be 1, 2, 1.

Sample Input 1
10
2
4
2
6
1
7
8
9
2
1

Sample Output 1
19

Explanation 1

Optimal distribution will be $1,2,1,2,1,2,3,4,2,1$

Sample Input 2
8
2
4
3
5
2
6
4
5

Sample Output 2
12

Explanation 2

Optimal distribution will be $12121212$.
"""

def minimum_candies(n, arr):
    if n == 0:
        return 0
    
    # Initialize arrays to store the number of candies needed for each child
    left = [0] * n
    right = [0] * n
    num = [0] * n
    
    # Fill the left array
    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            left[i] = left[i - 1] + 1
    
    # Fill the right array
    for i in range(n - 2, -1, -1):
        if arr[i] > arr[i + 1]:
            right[i] = right[i + 1] + 1
    
    # Calculate the total number of candies needed
    total_candies = 0
    for i in range(n):
        num[i] = 1 + max(left[i], right[i])
        total_candies += num[i]
    
    return total_candies