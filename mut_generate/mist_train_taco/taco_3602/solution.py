"""
QUESTION:
There are K pieces of cakes. Mr. Takahashi would like to eat one cake per day, taking K days to eat them all.

There are T types of cake, and the number of the cakes of type i (1 ≤ i ≤ T) is a_i.

Eating the same type of cake two days in a row would be no fun, so Mr. Takahashi would like to decide the order for eating cakes that minimizes the number of days on which he has to eat the same type of cake as the day before.

Compute the minimum number of days on which the same type of cake as the previous day will be eaten.

Constraints

* 1 ≤ K ≤ 10000
* 1 ≤ T ≤ 100
* 1 ≤ a_i ≤ 100
* a_1 + a_2 + ... + a_T = K

Input

The input is given from Standard Input in the following format:


K T
a_1 a_2 ... a_T


Output

Print the minimum number of days on which the same type of cake as the previous day will be eaten.

Examples

Input

7 3
3 2 2


Output

0


Input

6 3
1 4 1


Output

1


Input

100 1
100


Output

99
"""

def min_same_cake_days(K, T, a):
    # Calculate the maximum number of cakes of any single type
    max_cakes = max(a)
    
    # Calculate the minimum number of days on which the same type of cake as the previous day will be eaten
    result = max(0, 2 * (max_cakes - (K + 1) // 2) - 1)
    
    return result