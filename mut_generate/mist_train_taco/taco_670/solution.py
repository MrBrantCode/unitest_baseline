"""
QUESTION:
Jigar got a sequence of n positive integers as his birthday present! He likes consecutive subsequences whose sum is divisible by k. He asks you to write a program to count them for him.

Input Format 

The first line contains T, the number of testcases. 

T testcases follow. Each testcase consists of 2 lines. 

The first line contains n and k separated by a single space. 

And the second line contains n space separated integers.

Output Format 

For each test case, output the number of consecutive subsequenences whose sum is divisible by k in a newline.

Constraints 

1 ≤ T ≤ 20 

1 ≤ n ≤ 10^{6} 

1 ≤ k ≤ 100 

1 ≤ a[i] ≤ 10^{4} 

Sample Input

2
5 3
1 2 3 4 1
6 2
1 2 1 2 1 2

Sample Output

4
9

Explanation

For 

1 2 3 4 1

there exists, 4 subsequences whose sum is divisible by 3, they are   

3
1 2
1 2 3
2 3 4

For 

1 2 1 2 1 2

there exists, 9 subsequences whose sum is divisible by 2, they are  

2
2
2
1 2 1
1 2 1
1 2 1 2
2 1 2 1
1 2 1 2
2 1 2 1 2
"""

def count_divisible_subsequences(a, k):
    """
    Counts the number of consecutive subsequences in the list 'a' whose sum is divisible by 'k'.

    Parameters:
    a (list of int): The sequence of integers.
    k (int): The divisor.

    Returns:
    int: The number of consecutive subsequences whose sum is divisible by 'k'.
    """
    import itertools
    
    # Calculate the prefix sums modulo k
    a = itertools.accumulate(map(lambda x: x % k, a), lambda x, y: (x + y) % k)
    
    # Initialize a count array for remainders
    cnt = [0] * k
    
    # Count the occurrences of each remainder
    for x in a:
        cnt[x] += 1
    
    # Calculate the number of valid subsequences
    return sum((x * (x - 1) // 2 for x in cnt))