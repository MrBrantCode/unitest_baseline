"""
QUESTION:
You are given an array of integers $a_1, a_2, \ldots, a_n$ and an integer $x$.

You need to select the maximum number of elements in the array, such that for every subsegment $a_l, a_{l + 1}, \ldots, a_r$ containing strictly more than one element $(l < r)$, either:

At least one element on this subsegment is not selected, or

$a_l + a_{l+1} + \ldots + a_r \geq x \cdot (r - l + 1)$.


-----Input-----

The first line of input contains one integer $t$ ($1 \leq t \leq 10$): the number of test cases.

The descriptions of $t$ test cases follow, three lines per test case.

In the first line you are given one integer $n$ ($1 \leq n \leq 50000$): the number of integers in the array.

The second line contains $n$ integers $a_1, a_2, \ldots, a_n$ ($-100000 \leq a_i \leq 100000$).

The third line contains one integer $x$ ($-100000 \leq x \leq 100000$).


-----Output-----

For each test case, print one integer: the maximum number of elements that you can select.


-----Examples-----

Input
4
5
1 2 3 4 5
2
10
2 4 2 4 2 4 2 4 2 4
3
3
-10 -5 -10
-8
3
9 9 -3
5
Output
4
8
2
2


-----Note-----

In the first example, one valid way to select the elements is $[\underline{1}, 2, \underline{3}, \underline{4}, \underline{5}]$. All subsegments satisfy at least one of the criteria. For example, for the subsegment $l = 1$, $r = 2$ we have that the element $2$ is not selected, satisfying the first criterion. For the subsegment $l = 3$, $r = 5$ we have $3 + 4 + 5 = 12 \ge 2 \cdot 3$, satisfying the second criterion.

We can't select all elements, because in this case for $l = 1$, $r = 2$ all elements are selected and we have $a_1 + a_2 = 3 < 2 \cdot 2$. Thus, the maximum number of selected elements is $4$.

In the second example, one valid solution is $[\underline{2}, \underline{4}, 2, \underline{4}, \underline{2}, \underline{4}, 2, \underline{4}, \underline{2}, \underline{4}]$.

In the third example, one valid solution is $[\underline{-10}, -5, \underline{-10}]$.

In the fourth example, one valid solution is $[\underline{9}, \underline{9}, -3]$.
"""

def max_selected_elements(n, a, x):
    """
    Calculate the maximum number of elements that can be selected from the array `a`
    such that for every subsegment containing strictly more than one element, either:
    - At least one element on this subsegment is not selected, or
    - The sum of the elements in the subsegment is at least `x` times the length of the subsegment.

    Parameters:
    - n (int): The number of integers in the array.
    - a (list of int): The array of integers.
    - x (int): The integer threshold value.

    Returns:
    - int: The maximum number of elements that can be selected.
    """
    a = [c - x for c in a]
    begin = True
    unchosen = 0
    sum = 0
    for i in range(n):
        if begin:
            sum = a[i]
            begin = False
        else:
            sum += a[i]
            if sum < 0:
                begin = True
                unchosen += 1
            else:
                sum = min(sum, a[i])
    return n - unchosen