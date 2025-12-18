"""
QUESTION:
You have a large electronic screen which can display up to $998244353$ decimal digits. The digits are displayed in the same way as on different electronic alarm clocks: each place for a digit consists of $7$ segments which can be turned on and off to compose different digits. The following picture describes how you can display all $10$ decimal digits:

[Image]

As you can see, different digits may require different number of segments to be turned on. For example, if you want to display $1$, you have to turn on $2$ segments of the screen, and if you want to display $8$, all $7$ segments of some place to display a digit should be turned on.

You want to display a really large integer on the screen. Unfortunately, the screen is bugged: no more than $n$ segments can be turned on simultaneously. So now you wonder what is the greatest integer that can be displayed by turning on no more than $n$ segments.

Your program should be able to process $t$ different test cases.


-----Input-----

The first line contains one integer $t$ ($1 \le t \le 100$) — the number of test cases in the input.

Then the test cases follow, each of them is represented by a separate line containing one integer $n$ ($2 \le n \le 10^5$) — the maximum number of segments that can be turned on in the corresponding testcase.

It is guaranteed that the sum of $n$ over all test cases in the input does not exceed $10^5$.


-----Output-----

For each test case, print the greatest integer that can be displayed by turning on no more than $n$ segments of the screen. Note that the answer may not fit in the standard $32$-bit or $64$-bit integral data type.


-----Example-----
Input
2
3
4

Output
7
11
"""

def greatest_integer_for_segments(t: int, n_list: list) -> list:
    """
    Calculate the greatest integer that can be displayed on a screen with a given number of segments.

    Parameters:
    t (int): The number of test cases.
    n_list (list): A list of integers where each integer represents the maximum number of segments that can be turned on for each test case.

    Returns:
    list: A list of strings where each string represents the greatest integer that can be displayed for each corresponding test case.
    """
    results = []
    for n in n_list:
        int_part = n // 2
        ost = n - int_part * 2
        number = ''
        for i in range(int_part - 1):
            number += '1'
        if ost == 0:
            number += '1'
        else:
            number = '7' + number
        results.append(number)
    return results