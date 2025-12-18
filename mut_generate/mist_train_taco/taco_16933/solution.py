"""
QUESTION:
Rashmi loves the festival of Diwali as she gets to spend time with family and enjoy the festival. Before she can fully enjoy the festival she needs to complete the homework assigned by her teacher. Since Rashmi is smart , she has solved all the problems but is struck at one tricky pattern question.
Your Task is to help Rashmi solve the problem so that she can enjoy the festival with her family.
The Problem she is struck on is defined like this:
Given an integer N you need to generate the pattern according to following example:
Example:

Input:

3  
Output:

1 4 10

2 5 11

4 10 22

3 6 12  

-----Input:-----
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The next line of each contains T space separated integers N.

-----Output:-----
For each N print the required pattern.

-----Constraints:-----
$1 \leq T \leq 10^5$
$1 \leq N \leq 30$

-----Sample Input:-----
2
3 5

-----Sample Output:-----
1 4 10

2 5 11

4 10 22

3 6 12

1 4 10 22 46

2 5 11 23 47

4 10 22 46 94

3 6 12 24 48  

-----Sample Input:-----
1

4  

-----Sample Output:-----
1 4 10 22

2 5 11 23

4 10 22 46

3 6 12 24
"""

def generate_diwali_pattern(T, N_list):
    results = []
    
    for n in N_list:
        a = [1]
        b = [2]
        c = [4]
        d = [3]
        j = 1
        
        for i in range(n - 1):
            a.append(a[i] + 3 * j)
            b.append(b[i] + 3 * j)
            c.append(c[i] + 6 * j)
            d.append(d[i] + 3 * j)
            j *= 2
        
        results.append([a, b, c, d])
    
    return results