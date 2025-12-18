"""
QUESTION:
Dima got into number sequences. Now he's got sequence a_1, a_2, ..., a_{n}, consisting of n positive integers. Also, Dima has got a function f(x), which can be defined with the following recurrence:  f(0) = 0;  f(2·x) = f(x);  f(2·x + 1) = f(x) + 1. 

Dima wonders, how many pairs of indexes (i, j) (1 ≤ i < j ≤ n) are there, such that f(a_{i}) = f(a_{j}). Help him, count the number of such pairs. 


-----Input-----

The first line contains integer n (1 ≤ n ≤ 10^5). The second line contains n positive integers a_1, a_2, ..., a_{n} (1 ≤ a_{i} ≤ 10^9).

The numbers in the lines are separated by single spaces.


-----Output-----

In a single line print the answer to the problem.

Please, don't use the %lld specifier to read or write 64-bit integers in C++. It is preferred to use the cin, cout streams or the %I64d specifier.


-----Examples-----
Input
3
1 2 4

Output
3

Input
3
5 3 1

Output
1



-----Note-----

In the first sample any pair (i, j) will do, so the answer is 3.

In the second sample only pair (1, 2) will do.
"""

def count_f_equal_pairs(n, a):
    def helper(x):
        ret = 0
        while x > 0:
            if x % 2 == 0:
                x //= 2
            else:
                ret += 1
                x //= 2
        return ret
    
    # Initialize a list to count occurrences of each f(x) value
    d = [0] * 10000
    
    # Calculate f(x) for each element in the sequence and count occurrences
    for element in a:
        res = helper(element)
        d[res] += 1
    
    # Calculate the number of pairs (i, j) such that f(a[i]) == f(a[j])
    ans = 0
    for count in d:
        if count > 1:
            ans += count * (count - 1) // 2
    
    return ans