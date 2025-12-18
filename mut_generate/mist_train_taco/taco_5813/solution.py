"""
QUESTION:
Given a triplet of integers (X , Y , Z), such that X ≤ Y and Y ≥ Z, we define f(X , Y , Z) to be (X + Y) * (Y + Z). If either X > Y or Y < Z, or both, then f(X , Y , Z) is defined to be 0.
You are provided three arrays  A , B and C   of any length (their lengths may or may not be equal).  
Your task is to find the sum of f(X , Y , Z) over all triplets (X, Y , Z) where   X, Y and Z  belong to  A, B and C respectively.
Output your sum for each test case modulo 1000000007.

-----Input-----
- The first line contains a single integer, T, which is the number of test cases. The description of each testcase follows:
- The first line of each testcase contains 3 integers: p, q and r. These denote the lengths of A,B and C respectively. 
- The second line contains p integers, which are the elements of A
- The third line contains q integers, which are the elements of B
- The fourth line contains r integers, which are the elements of C

-----Output-----
Output the required sum modulo  1000000007  for each test case in a new line.

-----Constraints-----
- 1 ≤ T ≤ 10 
- 1 ≤ p, q, r ≤ 100000 
- 1 ≤ every array element ≤ 1000000000

-----Subtasks  -----
- Subtask #1 (30 points): 1 ≤ p,q,r  ≤ 100 
- Subtask #2 (70 points): 1 ≤ p,q,r  ≤ 100000 

-----Example : -----
Input:
1 
3 1 3
1 2 3
5
4 5 6

Output:
399

-----Explanation: -----
As there is only one choice for Y which equals to 5, to get a non-zero function value,we can choose any element for X from the set { 1 , 2 , 3 } and for Z from the set { 4  , 5 } 
So triplets which give non-zero function values are: 
{ 1 , 5  , 4 } :  ( 1 + 5 ) * ( 5 + 4 )  = 54 
{ 1 , 5  , 5 } :  ( 1 + 5 ) * ( 5 + 5 )  = 60 
{ 2 , 5  , 4 } :  ( 2 + 5 ) * ( 5 + 4 )  = 63 
{ 2 , 5  , 5 } :  ( 2 + 5 ) * ( 5 + 5 )  = 70 
{ 3 , 5  , 4 } :  ( 3 + 5 ) * ( 5 + 4 )  = 72 
{ 3 , 5  , 5 } :  ( 3 + 5 ) * ( 5 + 5 )  = 80 
Final answer : 54 + 60 + 63 + 70 + 72 + 80  = 399
"""

def calculate_triplet_sum(A, B, C, mod_value=1000000007):
    A.sort()
    B.sort()
    C.sort()
    
    x_sum = []
    z_sum = []
    
    if B[-1] < A[0] or B[-1] < C[0]:
        return 0
    
    count = 0
    for x in A:
        count += x
        x_sum.append(count)
    
    count = 0
    for z in C:
        count += z
        z_sum.append(count)
    
    y_counter = 0
    x_counter = 0
    z_counter = 0
    triplet_sum = 0
    
    while y_counter < len(B):
        while x_counter < len(A) and A[x_counter] <= B[y_counter]:
            x_counter += 1
        while z_counter < len(C) and C[z_counter] <= B[y_counter]:
            z_counter += 1
        
        if x_counter == 0 or z_counter == 0:
            y_counter += 1
            continue
        
        a = (x_sum[x_counter - 1] + x_counter * B[y_counter]) % mod_value
        b = (z_sum[z_counter - 1] + z_counter * B[y_counter]) % mod_value
        triplet_sum += a * b
        y_counter += 1
    
    return triplet_sum % mod_value