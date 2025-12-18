"""
QUESTION:
-----
CHEF N TIMINGS
-----

One day chef was working with some random numbers. Then he found something
interesting. He observed that no 240, 567, 9999 and 122 and called these numbers
nice as the digits in numbers are in increasing order. Also he called 434, 452, 900
are not nice as digits are in decreasing order

	

Now you are given a no and chef
wants you to find out largest "nice" integer which is smaller than or equal to the
given integer.

		
		

-----Constraints-----

1< t < 1000 

1< N < 10^18
	

-----Input Format-----

First line contains no. of test cases t. Then t test cases follow. Each test case
contain a integer n.

-----Output-----

Output a integer for each test case in a new line which is largest nice
integer smaller or equal to the given integer. 

		
		

-----Example Text Case-----
Input:

1
132

Output:

129
"""

def find_largest_nice_integer(n: str) -> str:
    n = [ele for ele in n]
    l = len(n)
    m = 10 ** 18 + 8
    ini = 1
    
    for i in range(l - 1, -1, -1):
        if int(n[i]) <= m:
            if ini == 1:
                m = int(n[i])
            else:
                m = max(m, int(n[i]))
        else:
            m = int(n[i]) - 1
            n[i] = str(m)
            for j in range(l - 1, i, -1):
                n[j] = '9'
    
    i = 0
    while n[i] == '0':
        i += 1
    
    return ''.join(n[i:])