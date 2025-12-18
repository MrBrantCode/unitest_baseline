"""
QUESTION:
Polycarp doesn't like integers that are divisible by $3$ or end with the digit $3$ in their decimal representation. Integers that meet both conditions are disliked by Polycarp, too.

Polycarp starts to write out the positive (greater than $0$) integers which he likes: $1, 2, 4, 5, 7, 8, 10, 11, 14, 16, \dots$. Output the $k$-th element of this sequence (the elements are numbered from $1$).


-----Input-----

The first line contains one integer $t$ ($1 \le t \le 100$) — the number of test cases. Then $t$ test cases follow.

Each test case consists of one line containing one integer $k$ ($1 \le k \le 1000$).


-----Output-----

For each test case, output in a separate line one integer $x$ — the $k$-th element of the sequence that was written out by Polycarp.


-----Examples-----

Input
10
1
2
3
4
5
6
7
8
9
1000
Output
1
2
4
5
7
8
10
11
14
1666


-----Note-----

None
"""

def find_polycarp_numbers(t: int, k_list: list) -> list:
    """
    Finds the k-th element in the sequence of numbers that Polycarp likes.

    Parameters:
    t (int): The number of test cases.
    k_list (list): A list of integers where each integer represents the position k in the sequence.

    Returns:
    list: A list of integers where each integer is the k-th element of the sequence for each test case.
    """
    arr = []
    i = 1
    while len(arr) <= max(k_list):
        if i % 3 != 0 and i % 10 != 3:
            arr.append(i)
        i += 1
    
    result = [arr[k - 1] for k in k_list]
    return result