"""
QUESTION:
John designs the following lower triangular matrix :

1 0 0 0 0 0 ...
2 2 0 0 0 0 ...
3 3 3 0 0 0 ...
4 4 4 4 0 0 ... 
5 5 5 5 5 0 ... 
6 6 6 6 6 6 ...
and so on ...

He represented this matrix as [R , C] , where R is the number of rows and C is the number of columns in the matrix.

Now he provides any random R and C to Ricky and asks him to tell the count of even and odd numbers in the matrix respectively.

Note: 0 is neither even nor odd.

Input:

First line contains number of test cases T.Each test case contains two integers R and C.

Output

For each test case  print count of even and odd numbers in  matrix [R,C].

Constraints:

1 ≤ T ≤ 100000

1 ≤ R ≤ 100000

1 ≤ C ≤ 100000

SAMPLE INPUT
3
2 3
6 7
10 10

SAMPLE OUTPUT
2 1
12 9
30 25
"""

def count_even_odd_in_matrix(R, C):
    """
    Counts the number of even and odd numbers in a lower triangular matrix of size R x C.

    Parameters:
    R (int): Number of rows in the matrix.
    C (int): Number of columns in the matrix.

    Returns:
    tuple: A tuple containing the count of even numbers and odd numbers in the matrix.
    """
    even_count = 0
    odd_count = 0
    
    while R > 0:
        if R % 2 == 0:
            even_count += min(R, C)
        else:
            odd_count += min(R, C)
        R -= 1
    
    return even_count, odd_count