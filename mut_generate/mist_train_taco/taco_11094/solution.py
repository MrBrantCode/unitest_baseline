"""
QUESTION:
I have a sequence defined as follows:

* All even-numbered terms are equal to the previous term multiplied by 2.
* All odd-numbered terms are equal to the previous term divided by 3.



Create a program that reads the first term a of this sequence and outputs the sum s (10) from the first term to the tenth term.



Input

The input consists of multiple test cases. For each test case, a real number a (1.0 ≤ a ≤ 10.0) representing the first term of the sequence is given in one row.

The number of test cases does not exceed 50.

Output

Print s (10) on one line for each test case.

The output may contain an error of 0.000001 or less.

Example

Input

1.0
2.0
3.0


Output

7.81481481
15.62962963
23.44444444
"""

def calculate_sequence_sum(a1: float) -> float:
    """
    Calculate the sum of the first 10 terms of a sequence defined by:
    - All even-numbered terms are equal to the previous term multiplied by 2.
    - All odd-numbered terms are equal to the previous term divided by 3.

    Parameters:
    a1 (float): The first term of the sequence.

    Returns:
    float: The sum of the first 10 terms of the sequence.
    """
    lst = [a1]
    for i in range(2, 11):
        if i % 2:
            a1 /= 3
        else:
            a1 *= 2
        lst.append(a1)
    return sum(lst)