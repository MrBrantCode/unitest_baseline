"""
QUESTION:
Read problem statements in [Hindi], [Bengali], [Mandarin Chinese], [Russian], and [Vietnamese] as well.

Guddu likes a girl that loves playing with numbers. She agreed to go on a date with Guddu, but only if he can solve the following problem:

An integer is *round* if it is greater than $0$ and the sum of its digits in decimal representation is a multiple of $10$. Find the $N$-th smallest round integer.

However, Guddu does not like playing with numbers at all and he is unable to solve this problem, so he begs you to solve it for him. In return, he will definitely give you a treat.

------  Input ------
The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
The first and only line of each test case contains a single integer $N$.

------  Output ------
For each test case, print a single line containing the $N$-th round integer. It is guaranteed that this number is smaller than $2^{64}$.

------  Constraints ------
$1 ≤ T ≤ 10^{5}$
$1 ≤ N ≤ 10^{18}$

------  Subtasks ------
Subtask #1 (30 points):
$1 ≤ T ≤ 10$
$1 ≤ N ≤ 10^{5}$

Subtask #2 (70 points): original constraints

----- Sample Input 1 ------ 
1

2
----- Sample Output 1 ------ 
28
----- explanation 1 ------ 
Example case 1: The smallest round integer is $19$ and the second smallest is $28$.
"""

def find_nth_round_integer(n: int) -> int:
    # Convert the position to a string to manipulate digits
    n_str = str(n)
    
    # Calculate the sum of the digits of n
    digit_sum = sum(int(digit) for digit in n_str)
    
    # Calculate the last digit to make the sum a multiple of 10
    last_digit = (10 - (digit_sum % 10)) % 10
    
    # Construct the round integer by appending the last digit to n
    round_integer = int(n_str + str(last_digit))
    
    return round_integer