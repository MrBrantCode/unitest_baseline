"""
QUESTION:
You are given a pair of integers $(a, b)$ and an integer $x$.

You can change the pair in two different ways:

set (assign) $a := |a - b|$;

set (assign) $b := |a - b|$,

where $|a - b|$ is the absolute difference between $a$ and $b$.

The pair $(a, b)$ is called $x$-magic if $x$ is obtainable either as $a$ or as $b$ using only the given operations (i.e. the pair $(a, b)$ is $x$-magic if $a = x$ or $b = x$ after some number of operations applied). You can apply the operations any number of times (even zero).

Your task is to find out if the pair $(a, b)$ is $x$-magic or not.

You have to answer $t$ independent test cases.


-----Input-----

The first line of the input contains one integer $t$ ($1 \le t \le 10^4$) — the number of test cases. The next $t$ lines describe test cases.

The only line of the test case contains three integers $a$, $b$ and $x$ ($1 \le a, b, x \le 10^{18}$).


-----Output-----

For the $i$-th test case, print YES if the corresponding pair $(a, b)$ is $x$-magic and NO otherwise.


-----Examples-----

Input
8
6 9 3
15 38 7
18 8 8
30 30 30
40 50 90
24 28 20
365 216 52
537037812705867558 338887693834423551 3199921013340
Output
YES
YES
YES
YES
NO
YES
YES
YES


-----Note-----

None
"""

def is_x_magic(a: int, b: int, x: int) -> bool:
    """
    Determines if the pair (a, b) is x-magic.

    Parameters:
    a (int): The first integer in the pair.
    b (int): The second integer in the pair.
    x (int): The target integer to check if it can be obtained.

    Returns:
    bool: True if the pair (a, b) is x-magic, False otherwise.
    """
    a, b = max(a, b), min(a, b)
    if x > a:
        return False
    while b > 0 and a >= x:
        if (a - x) % b == 0:
            return True
        a, b = b, a % b
    return a == x