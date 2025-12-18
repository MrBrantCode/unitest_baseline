"""
QUESTION:
A robber has attempted to rob a bank but failed to complete his task. However, he had managed to open all the safes.

Oleg the bank client loves money (who doesn't), and decides to take advantage of this failed robbery and steal some money from the safes. There are many safes arranged in a line, where the i-th safe from the left is called safe i. There are n banknotes left in all the safes in total. The i-th banknote is in safe x_{i}. Oleg is now at safe a. There are two security guards, one of which guards the safe b such that b < a, i.e. the first guard is to the left of Oleg. The other guard guards the safe c so that c > a, i.e. he is to the right of Oleg.

The two guards are very lazy, so they do not move. In every second, Oleg can either take all the banknotes from the current safe or move to any of the neighboring safes. However, he cannot visit any safe that is guarded by security guards at any time, becaues he might be charged for stealing. Determine the maximum amount of banknotes Oleg can gather.


-----Input-----

The first line of input contains three space-separated integers, a, b and c (1 ≤ b < a < c ≤ 10^9), denoting the positions of Oleg, the first security guard and the second security guard, respectively.

The next line of input contains a single integer n (1 ≤ n ≤ 10^5), denoting the number of banknotes.

The next line of input contains n space-separated integers x_1, x_2, ..., x_{n} (1 ≤ x_{i} ≤ 10^9), denoting that the i-th banknote is located in the x_{i}-th safe. Note that x_{i} are not guaranteed to be distinct.


-----Output-----

Output a single integer: the maximum number of banknotes Oleg can take.


-----Examples-----
Input
5 3 7
8
4 7 5 5 3 6 2 8

Output
4

Input
6 5 7
5
1 5 7 92 3

Output
0



-----Note-----

In the first example Oleg can take the banknotes in positions 4, 5, 6 (note that there are 2 banknotes at position 5). Oleg can't take the banknotes in safes 7 and 8 because he can't run into the second security guard. Similarly, Oleg cannot take the banknotes at positions 3 and 2 because he can't run into the first security guard. Thus, he can take a maximum of 4 banknotes.

For the second sample, Oleg can't take any banknotes without bumping into any of the security guards.
"""

def max_banknotes_gathered(a: int, b: int, c: int, banknotes: list) -> int:
    """
    Calculate the maximum number of banknotes Oleg can gather without encountering the security guards.

    Parameters:
    a (int): The position of Oleg.
    b (int): The position of the first security guard (left of Oleg).
    c (int): The position of the second security guard (right of Oleg).
    banknotes (list): A list of integers representing the positions of the banknotes.

    Returns:
    int: The maximum number of banknotes Oleg can gather.
    """
    count = 0
    for position in banknotes:
        if b < position < c:
            count += 1
    return count