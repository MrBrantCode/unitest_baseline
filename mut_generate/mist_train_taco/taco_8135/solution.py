"""
QUESTION:
Let's call a number k-good if it contains all digits not exceeding k (0, ..., k). You've got a number k and an array a containing n numbers. Find out how many k-good numbers are in a (count each number every time it occurs in array a).


-----Input-----

The first line contains integers n and k (1 ≤ n ≤ 100, 0 ≤ k ≤ 9). The i-th of the following n lines contains integer a_{i} without leading zeroes (1 ≤ a_{i} ≤ 10^9).


-----Output-----

Print a single integer — the number of k-good numbers in a.


-----Examples-----
Input
10 6
1234560
1234560
1234560
1234560
1234560
1234560
1234560
1234560
1234560
1234560

Output
10

Input
2 1
1
10

Output
1
"""

def count_k_good_numbers(n: int, k: int, a: list) -> int:
    """
    Counts the number of k-good numbers in the array `a`.

    A number is considered k-good if it contains all digits from 0 to k at least once.

    Parameters:
    - n (int): The number of elements in the array `a`.
    - k (int): The maximum digit that should be present in the k-good numbers.
    - a (list): The array of numbers to be checked.

    Returns:
    - int: The number of k-good numbers in the array `a`.
    """
    bad = 0
    for number in a:
        for digit in range(k + 1):
            if str(digit) not in number:
                bad += 1
                break
    return n - bad