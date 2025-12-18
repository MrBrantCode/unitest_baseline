"""
QUESTION:
You are given a sequence $a_1, a_2, \dots, a_n$ consisting of $n$ non-zero integers (i.e. $a_i \ne 0$). 

You have to calculate two following values:  the number of pairs of indices $(l, r)$ $(l \le r)$ such that $a_l \cdot a_{l + 1} \dots a_{r - 1} \cdot a_r$ is negative;  the number of pairs of indices $(l, r)$ $(l \le r)$ such that $a_l \cdot a_{l + 1} \dots a_{r - 1} \cdot a_r$ is positive; 


-----Input-----

The first line contains one integer $n$ $(1 \le n \le 2 \cdot 10^{5})$ — the number of elements in the sequence.

The second line contains $n$ integers $a_1, a_2, \dots, a_n$ $(-10^{9} \le a_i \le 10^{9}; a_i \neq 0)$ — the elements of the sequence.


-----Output-----

Print two integers — the number of subsegments with negative product and the number of subsegments with positive product, respectively.


-----Examples-----
Input
5
5 -3 3 -1 1

Output
8 7

Input
10
4 2 -4 3 1 2 -4 3 2 3

Output
28 27

Input
5
-1 -2 -3 -4 -5

Output
9 6
"""

def count_subsegment_products(n, a):
    # Convert the sequence to a list of signs (1 for positive, -1 for negative)
    a = [1 if x > 0 else -1 for x in a]
    
    # Initialize variables
    last = 0
    pr = 1
    
    # Calculate the number of positive subsegments ending at each position
    for q in a:
        pr *= q
        if pr > 0:
            last += 1
    
    # Initialize the answer with the count of positive subsegments ending at the last position
    ans = last
    
    # Update the count of positive subsegments for each starting position
    for q in range(1, len(a)):
        if a[q - 1] > 0:
            last -= 1
        else:
            last = n - q - last
        ans += last
    
    # Total subsegments are n * (n + 1) // 2
    total_subsegments = n * (n + 1) // 2
    
    # The number of negative subsegments is the total minus the number of positive subsegments
    negative_subsegments = total_subsegments - ans
    
    return (negative_subsegments, ans)