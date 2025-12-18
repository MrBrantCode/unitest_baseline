"""
QUESTION:
Read problems statements in Mandarin Chinese, Russian and Vietnamese as well. 

Chef loves Tetris. He keeps on playing Tetris all the time. Today Chef's mother wanted to him play something else and brought an array for her son. That is why Chef now decided to play Tetris with arrays. Here are the rules of the game:

Chef has an array A consisting of N positive integers. This is a base array. 
Chef has an array B consisting of N positive integers. He placed this array directly above the array A. Imagine that array B is falling on array A, such that number B_{i} is directly above the number A_{i} initially.
If element B_{i} falls on A_{i}, A_{i} gets increased by B_{i}. 
Each element B_{i} can be dropped by Chef on either A_{i-1}, A_{i} or A_{i+1}.
Chef can't drop element out of array (for example he can't drop B_{0} on A_{-1}). 
Chef wants all the elements of array A to become equal, and looking for the biggest possible value he can get. 

Please help Chef in enjoying the game!!

------ Input ------ 

The first line of the input contains an integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains a single integer N denoting the number of elements in both arrays. 
The second line contains N space-separated integers B_{1}, B_{2}, ..., B_{N} denoting the elements of the falling array. 
The third line contains N space-separated integers A_{1}, A_{2}, ..., A_{N} denoting the elements of the base array. 

------ Output ------ 

For each test case, output a single line containing a biggest integer Chef can get for all elements of array A or -1 if it is impossible. 

------ Constraints ------ 

$1 ≤ T ≤ 5$
$1 ≤ N ≤ 10^{4}$
$1 ≤ A_{i} ≤ 10^{6}$
$1 ≤ B_{i} ≤ 10^{6}$

------ Subtasks ------ 

$Subtask N ≤ 15. Points: 30 $
$Subtask N ≤ 10^{4}. Points: 70 $

----- Sample Input 1 ------ 
3

1

10

20

4

15 7 10 10

6 14 21 1

3

1 100 3

1 2 3
----- Sample Output 1 ------ 
30

21

-1
----- explanation 1 ------ 
Example case 1.
The only option in first example is to make 10 fall on 20. As we have only one element condition of equality is satisfied. 

Example case 2.
Here Chef makes 15 fall on 6, 7 fall on 14, an then both elements with value 10 should fall on 1. Then all elements will become 21.

Example case 3.
There is no way for Chef to make all elements of a base array equal.
"""

def maximize_array_elements(a, b, n):
    # Calculate the total sum of elements in both arrays
    total_sum = sum(a) + sum(b)
    
    # If the total sum is not divisible by n, it's impossible to make all elements equal
    if total_sum % n != 0:
        return -1
    
    # Calculate the target value for each element in array a
    target_value = total_sum // n
    
    # Check if the first element can be made equal to the target value
    if a[0] + b[0] == target_value:
        b[0] = 0
    elif a[0] + b[1] == target_value:
        b[1] = 0
    elif a[0] + b[0] + b[1] == target_value:
        b[0], b[1] = 0, 0
    elif a[0] != target_value:
        return -1
    
    # Check if the last element can be made equal to the target value
    if a[n - 1] + b[n - 1] == target_value:
        b[n - 1] = 0
    elif a[n - 1] + b[n - 2] == target_value:
        b[n - 2] = 0
    elif a[n - 1] + b[n - 1] + b[n - 2] == target_value:
        b[n - 1], b[n - 2] = 0, 0
    elif a[n - 1] != target_value:
        return -1
    
    # Iterate through the middle elements and check if they can be made equal to the target value
    for i in range(1, n - 1):
        a[i] += b[i - 1]
        b[i - 1] = 0
        if a[i] + b[i] == target_value:
            b[i] = 0
        elif a[i] + b[i + 1] == target_value:
            b[i + 1] = 0
        elif a[i] + b[i] + b[i + 1] == target_value:
            b[i], b[i + 1] = 0, 0
        elif a[i] != target_value:
            return -1
    
    return target_value