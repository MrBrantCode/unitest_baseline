"""
QUESTION:
Alice recently converted all the positive integers from 1 to 2^{N} - 1 (both inclusive) into binary strings and stored them in an array S.  Note that the binary strings do not have leading zeroes.  
While she was out, Bob sorted all the elements of S in lexicographical increasing order.

Let S_{i} denotes the i^{th} string in the sorted array.  
Alice defined a function F such that F(S_{i}) is equal to the count of 1 in the string S_{i}.  
For example, F(101) = 2 and F(1000) = 1.
 
Given a positive integer K, find the value of \sum_{i = 1}^K F(S_{i}). 

String P is lexicographically smaller than string Q if one of the following satisfies:
P is a prefix of Q and P \neq Q.
There exists an index i such that P_{i} < Q_{i} and for all j < i,  P_{j}=Q_{j}.

------ Input Format ------ 

- The first line will contain an integer T - number of test cases. Then the test cases follow.
- The first and only line of each test case contains two integers N and K.

------ Output Format ------ 

For each test case, output the value \sum_{i = 1}^K F(S_{i}). 

------ Constraints ------ 

$1 ≤ T ≤ 3000$
$1 ≤ N ≤ 50$
$1 ≤ K ≤ 2^{N} - 1$
- Sum of $N$ over all test cases does not exceed $10^{5}$.

----- Sample Input 1 ------ 
3
3 2
3 4
3 7
----- Sample Output 1 ------ 
2
5
12

----- explanation 1 ------ 
Converting positive integers to Binary Strings:
- $1 = 1$
- $2 = 10$
- $3 = 11$
- $4 = 100$
- $5 = 101$
- $6 = 110$
- $7 = 111$

Sorting Binary Strings in lexicographical order:
After sorting, the strings will appear in the following order:  
$[1, 10, 100, 101, 11, 110, 111]$.

Test case $1$: $F(S_{1}) + F(S_{2}) = F(1) + F(10) = 1 + 1 = 2$.

Test case $2$: $F(S_{1}) + F(S_{2}) + F(S_{3}) + F(S_{4}) = F(1) + F(10) + F(100) + F(101) = 1 + 1 + 1 + 2 = 5$.
"""

def calculate_sum_of_F(N, K):
    """
    Calculate the sum of the function F applied to the first K elements of the sorted array S.

    Parameters:
    N (int): The maximum power of 2 used to generate the binary strings.
    K (int): The number of elements from the sorted array S to consider.

    Returns:
    int: The sum of the function F applied to the first K elements of the sorted array S.
    """
    z = [0 for _ in range(51)]
    z[1] = 1
    for i in range(2, 51):
        z[i] = 2 * z[i - 1] + 2 ** (i - 2)
    b = [0 for i in range(51)]
    for i in range(1, 51):
        b[i] = b[i - 1] + z[i]

    def sol1(target, n):
        value = 1
        sum1 = 1
        num1 = 1
        abnum = 2 ** (n - 1) - 1
        while value != target:
            if value + abnum > target:
                value = value + 1
                sum1 = sum1 + num1
                n = n - 1
                abnum = 2 ** (n - 1) - 1
            elif value + abnum < target:
                value = value + abnum + 1
                sum1 = sum1 + num1 * abnum
                n = n - 1
                for u in range(1, n):
                    sum1 = sum1 + b[u]
                num1 = num1 + 1
                sum1 = sum1 + num1
                abnum = 2 ** (n - 1) - 1
            else:
                value = value + abnum
                sum1 = sum1 + num1 * abnum
                n = n - 1
                for u in range(1, n):
                    sum1 = sum1 + b[u]
        return sum1

    return sol1(K, N)