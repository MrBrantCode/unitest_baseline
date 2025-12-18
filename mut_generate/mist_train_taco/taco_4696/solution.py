"""
QUESTION:
Taisia has $n$ six-sided dice. Each face of the die is marked with a number from $1$ to $6$, each number from $1$ to $6$ is used once.

Taisia rolls all $n$ dice at the same time and gets a sequence of values $a_1, a_2, \ldots, a_n$ ($1 \le a_i \le 6$), where $a_i$ is the value on the upper face of the $i$-th dice. The sum of this sequence is equal to $s$.

Suddenly, Taisia's pet cat steals exactly one dice with maximum value $a_i$ and calculates the sum of the values on the remaining $n-1$ dice, which is equal to $r$.

You only know the number of dice $n$ and the values of $s$, $r$. Restore a possible sequence $a$ that fulfills the constraints.


-----Input-----

The first line contains the integer $t$ ($1 \le t \le 1000$) — the number of testcases.

Each testcase is given on a separate line and contains three integers $n$, $s$, $r$ ($2 \le n \le 50$, $1 \le r < s \le 300$).

It is guaranteed that a solution exists.


-----Output-----

For each testcase, print: $n$ integers $a_1, a_2, \ldots, a_n$ in any order. It is guaranteed that such sequence exists.

If there are multiple solutions, print any.


-----Examples-----

Input
7
2 2 1
2 4 2
4 9 5
5 17 11
3 15 10
4 4 3
5 20 15
Output
1 1
2 2 
1 2 2 4
6 4 2 3 2
5 5 5
1 1 1 1
1 4 5 5 5


-----Note-----

None
"""

def restore_dice_sequence(n, s, r):
    """
    Restores a possible sequence of values on n dice given the sum s and the sum r of the remaining dice after one dice with the maximum value is removed.

    Parameters:
    n (int): The number of dice.
    s (int): The sum of the values on all dice.
    r (int): The sum of the values on the remaining dice after one dice with the maximum value is removed.

    Returns:
    list: A list of integers representing the sequence of values on the dice.
    """
    m = s - r  # The maximum value on the dice
    mas = []
    
    # Distribute the sum s into the dice values
    while s != 0:
        if s >= m:
            mas.extend([m] * (s // m))
            s %= m
        m -= 1
    
    # If the number of dice in mas is less than n, adjust the sequence
    if n == len(mas):
        return mas
    else:
        g = n - len(mas)
        while g != 0:
            for i in range(1, len(mas)):
                if mas[i] != 1:
                    mas[i] -= 1
                    mas.append(1)
                    g -= 1
                if g == 0:
                    return mas