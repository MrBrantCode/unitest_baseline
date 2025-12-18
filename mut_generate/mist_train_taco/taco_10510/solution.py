"""
QUESTION:
Polycarp has to solve exactly $n$ problems to improve his programming skill before an important programming competition. But this competition will be held very soon, most precisely, it will start in $k$ days. It means that Polycarp has exactly $k$ days for training!

Polycarp doesn't want to procrastinate, so he wants to solve at least one problem during each of $k$ days. He also doesn't want to overwork, so if he solves $x$ problems during some day, he should solve no more than $2x$ problems during the next day. And, at last, he wants to improve his skill, so if he solves $x$ problems during some day, he should solve at least $x+1$ problem during the next day.

More formally: let $[a_1, a_2, \dots, a_k]$ be the array of numbers of problems solved by Polycarp. The $i$-th element of this array is the number of problems Polycarp solves during the $i$-th day of his training. Then the following conditions must be satisfied:   sum of all $a_i$ for $i$ from $1$ to $k$ should be $n$;  $a_i$ should be greater than zero for each $i$ from $1$ to $k$;  the condition $a_i < a_{i + 1} \le 2 a_i$ should be satisfied for each $i$ from $1$ to $k-1$. 

Your problem is to find any array $a$ of length $k$ satisfying the conditions above or say that it is impossible to do it.


-----Input-----

The first line of the input contains two integers $n$ and $k$ ($1 \le n \le 10^9, 1 \le k \le 10^5$) — the number of problems Polycarp wants to solve and the number of days Polycarp wants to train.


-----Output-----

If it is impossible to find any array $a$ of length $k$ satisfying Polycarp's rules of training, print "NO" in the first line.

Otherwise print "YES" in the first line, then print $k$ integers $a_1, a_2, \dots, a_k$ in the second line, where $a_i$ should be the number of problems Polycarp should solve during the $i$-th day. If there are multiple answers, you can print any.


-----Examples-----
Input
26 6

Output
YES
1 2 4 5 6 8 

Input
8 3

Output
NO

Input
1 1

Output
YES
1 

Input
9 4

Output
NO
"""

def find_training_schedule(n, k):
    """
    Determines if Polycarp can solve exactly `n` problems over `k` days
    while adhering to the constraints:
    - Solve at least one problem each day.
    - Solve at least one more problem each subsequent day.
    - Solve no more than twice the number of problems of the previous day.

    Parameters:
    n (int): Total number of problems to solve.
    k (int): Number of days available for training.

    Returns:
    str or list: Returns "NO" if it is impossible to create the schedule.
                 Otherwise, returns a list of integers representing the number
                 of problems to solve each day.
    """
    
    # Check if it's impossible to create the schedule
    if k * (k + 1) // 2 > n:
        return "NO"
    
    # Calculate the base value for each day
    v = (n - k * (k + 1) // 2) // k
    a = [v + i for i in range(1, k + 1)]
    
    # Special cases for small k values
    if v == 0:
        if k == 2:
            if sum(a) != n:
                return "NO"
            else:
                return a
        elif k == 3:
            if n == 6:
                return a
            elif n == 7:
                return [1, 2, 4]
            else:
                return "NO"
        else:
            if n - sum(a) >= 2:
                a[-2] += 1
            a[-1] += n - sum(a)
            return a
    else:
        a[-1] += n - sum(a)
        return a