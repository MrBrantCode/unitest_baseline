"""
QUESTION:
After seeing the "ALL YOUR BASE ARE BELONG TO US" meme for the first time, numbers X and Y realised that they have different bases, which complicated their relations.

You're given a number X represented in base b_{x} and a number Y represented in base b_{y}. Compare those two numbers.


-----Input-----

The first line of the input contains two space-separated integers n and b_{x} (1 ≤ n ≤ 10, 2 ≤ b_{x} ≤ 40), where n is the number of digits in the b_{x}-based representation of X. 

The second line contains n space-separated integers x_1, x_2, ..., x_{n} (0 ≤ x_{i} < b_{x}) — the digits of X. They are given in the order from the most significant digit to the least significant one.

The following two lines describe Y in the same way: the third line contains two space-separated integers m and b_{y} (1 ≤ m ≤ 10, 2 ≤ b_{y} ≤ 40, b_{x} ≠ b_{y}), where m is the number of digits in the b_{y}-based representation of Y, and the fourth line contains m space-separated integers y_1, y_2, ..., y_{m} (0 ≤ y_{i} < b_{y}) — the digits of Y.

There will be no leading zeroes. Both X and Y will be positive. All digits of both numbers are given in the standard decimal numeral system.


-----Output-----

Output a single character (quotes for clarity):   '<' if X < Y  '>' if X > Y  '=' if X = Y 


-----Examples-----
Input
6 2
1 0 1 1 1 1
2 10
4 7

Output
=

Input
3 3
1 0 2
2 5
2 4

Output
<

Input
7 16
15 15 4 0 0 7 10
7 9
4 8 0 3 1 5 0

Output
>



-----Note-----

In the first sample, X = 101111_2 = 47_10 = Y.

In the second sample, X = 102_3 = 21_5 and Y = 24_5 = 112_3, thus X < Y.

In the third sample, $X = FF 4007 A_{16}$ and Y = 4803150_9. We may notice that X starts with much larger digits and b_{x} is much larger than b_{y}, so X is clearly larger than Y.
"""

def compare_numbers_in_bases(n, b_x, arrx, m, b_y, arry):
    """
    Compares two numbers X and Y represented in different bases.

    Parameters:
    n (int): Number of digits in the base b_x representation of X.
    b_x (int): Base of X.
    arrx (list[int]): List of digits of X.
    m (int): Number of digits in the base b_y representation of Y.
    b_y (int): Base of Y.
    arry (list[int]): List of digits of Y.

    Returns:
    str: A single character indicating the comparison result:
         '<' if X < Y
         '>' if X > Y
         '=' if X = Y
    """
    sumx = sumy = 0
    
    # Convert X from base b_x to decimal
    for i in range(n):
        sumx += pow(b_x, n - 1 - i) * arrx[i]
    
    # Convert Y from base b_y to decimal
    for j in range(m):
        sumy += pow(b_y, m - 1 - j) * arry[j]
    
    # Compare the two decimal values
    if sumx > sumy:
        return '>'
    elif sumx < sumy:
        return '<'
    else:
        return '='