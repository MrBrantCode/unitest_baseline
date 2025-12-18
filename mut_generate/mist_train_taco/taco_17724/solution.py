"""
QUESTION:
After finishing eating her bun, Alyona came up with two integers n and m. She decided to write down two columns of integers — the first column containing integers from 1 to n and the second containing integers from 1 to m. Now the girl wants to count how many pairs of integers she can choose, one from the first column and the other from the second column, such that their sum is divisible by 5.

Formally, Alyona wants to count the number of pairs of integers (x, y) such that 1 ≤ x ≤ n, 1 ≤ y ≤ m and $(x + y) \operatorname{mod} 5$ equals 0.

As usual, Alyona has some troubles and asks you to help.


-----Input-----

The only line of the input contains two integers n and m (1 ≤ n, m ≤ 1 000 000).


-----Output-----

Print the only integer — the number of pairs of integers (x, y) such that 1 ≤ x ≤ n, 1 ≤ y ≤ m and (x + y) is divisible by 5.


-----Examples-----
Input
6 12

Output
14

Input
11 14

Output
31

Input
1 5

Output
1

Input
3 8

Output
5

Input
5 7

Output
7

Input
21 21

Output
88



-----Note-----

Following pairs are suitable in the first sample case:   for x = 1 fits y equal to 4 or 9;  for x = 2 fits y equal to 3 or 8;  for x = 3 fits y equal to 2, 7 or 12;  for x = 4 fits y equal to 1, 6 or 11;  for x = 5 fits y equal to 5 or 10;  for x = 6 fits y equal to 4 or 9. 

Only the pair (1, 4) is suitable in the third sample case.
"""

def count_pairs_divisible_by_5(n, m):
    # Ensure n is the smaller value and m is the larger value
    n, m = min(n, m), max(n, m)
    
    # Calculate the total number of pairs divisible by 5
    total = m * (n // 5)
    
    # Calculate the remaining pairs that can be formed with the remainder of n and m
    z = n % 5 + m % 5
    f = z % 5 if z > 5 else 0
    
    total += n % 5 * (m // 5) + z // 5 + f
    
    return total