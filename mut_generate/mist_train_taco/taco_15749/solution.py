"""
QUESTION:
You are given an integer sequence of length n, a_1, ..., a_n.
Let us consider performing the following n operations on an empty sequence b.
The i-th operation is as follows:
 - Append a_i to the end of b.
 - Reverse the order of the elements in b.
Find the sequence b obtained after these n operations.

-----Constraints-----
 - 1 \leq n \leq 2\times 10^5
 - 0 \leq a_i \leq 10^9
 - n and a_i are integers.

-----Input-----
Input is given from Standard Input in the following format:
n
a_1 a_2 ... a_n

-----Output-----
Print n integers in a line with spaces in between.
The i-th integer should be b_i.

-----Sample Input-----
4
1 2 3 4

-----Sample Output-----
4 2 1 3

 - After step 1 of the first operation, b becomes: 1.
 - After step 2 of the first operation, b becomes: 1.
 - After step 1 of the second operation, b becomes: 1, 2.
 - After step 2 of the second operation, b becomes: 2, 1.
 - After step 1 of the third operation, b becomes: 2, 1, 3.
 - After step 2 of the third operation, b becomes: 3, 1, 2.
 - After step 1 of the fourth operation, b becomes: 3, 1, 2, 4.
 - After step 2 of the fourth operation, b becomes: 4, 2, 1, 3.
Thus, the answer is 4 2 1 3.
"""

def generate_sequence_b(n, a):
    o = [a[i] for i in range(0, n, 2)]
    e = [a[h] for h in range(1, n, 2)]
    
    if n % 2 == 0:
        e.reverse()
        l = e + o
    else:
        o.reverse()
        l = o + e
    
    return l