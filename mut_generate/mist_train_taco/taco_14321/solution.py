"""
QUESTION:
An exam for n students will take place in a long and narrow room, so the students will sit in a line in some order. The teacher suspects that students with adjacent numbers (i and i + 1) always studied side by side and became friends and if they take an exam sitting next to each other, they will help each other for sure.

Your task is to choose the maximum number of students and make such an arrangement of students in the room that no two students with adjacent numbers sit side by side.


-----Input-----

A single line contains integer n (1 ≤ n ≤ 5000) — the number of students at an exam.


-----Output-----

In the first line print integer k — the maximum number of students who can be seated so that no two students with adjacent numbers sit next to each other.

In the second line print k distinct integers a_1, a_2, ..., a_{k} (1 ≤ a_{i} ≤ n), where a_{i} is the number of the student on the i-th position. The students on adjacent positions mustn't have adjacent numbers. Formally, the following should be true: |a_{i} - a_{i} + 1| ≠ 1 for all i from 1 to k - 1.

If there are several possible answers, output any of them.


-----Examples-----
Input
6
Output
6
1 5 3 6 2 4
Input
3

Output
2
1 3
"""

def arrange_students(n: int) -> tuple[int, list[int]]:
    """
    Arrange the maximum number of students such that no two students with adjacent numbers sit next to each other.

    Parameters:
    n (int): The number of students.

    Returns:
    tuple[int, list[int]]: A tuple containing:
        - The maximum number of students who can be seated (k).
        - A list of k distinct integers representing the arrangement of students.
    """
    if n == 1 or n == 2:
        return 1, [1]
    elif n == 3:
        return 2, [1, 3]
    else:
        odd = [i for i in range(1, n + 1) if i % 2 != 0]
        even = [i for i in range(1, n + 1) if i % 2 == 0]
        return n, odd[::-1] + even[::-1]