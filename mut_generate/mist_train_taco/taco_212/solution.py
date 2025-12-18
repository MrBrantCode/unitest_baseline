"""
QUESTION:
FizzBuzz is a game in which integers of 1 or more are spoken in order according to the following rules.

* "Fizz" when divisible by 3

* "Buzz" when divisible by 5

* "FizzBuzz" when divisible by both 3 and 5

* At other times, that number




An example of the progress of the game is shown below.

1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz, 16,…

The character string obtained by combining the obtained remarks into one character string is called FizzBuzz String. Since the index s is given, output 20 characters from the s character of the FizzBuzz String. However, the index may start from 1, and the length of the obtained character string may be sufficiently large (s + 20 or more).

Constraints

* s is an integer

* 1 ≤ s ≤ 1018

Input

Input is given in the following format

> s
>

Output

Output 20 characters from the s character of FizzBuzz String on one line

Examples

Input

1


Output

12Fizz4BuzzFizz78Fiz


Input

20


Output

zzBuzz11Fizz1314Fizz


Input

10000000000


Output

93FizzBuzz1418650796
"""

def get_fizzbuzz_substring(s: int) -> str:
    def calc_start(mid: int) -> int:
        cnt = -1
        i = 1
        while 10 ** i < mid:
            cnt += i * (10 ** i - 10 ** (i - 1))
            fif = (10 ** i - 1) // 15 - (10 ** (i - 1) - 1) // 15
            three = (10 ** i - 1) // 3 - (10 ** (i - 1) - 1) // 3
            five = (10 ** i - 1) // 5 - (10 ** (i - 1) - 1) // 5
            cnt += (three + five) * 4 - (three + five - fif) * i
            i += 1
        cnt += i * (mid - 10 ** (i - 1))
        fif = (mid - 1) // 15 - (10 ** (i - 1) - 1) // 15
        three = (mid - 1) // 3 - (10 ** (i - 1) - 1) // 3
        five = (mid - 1) // 5 - (10 ** (i - 1) - 1) // 5
        cnt += (three + five) * 4 - (three + five - fif) * i
        return cnt + 1

    N = s - 1
    (left, right) = (1, 10 ** 18)
    while left + 1 < right:
        mid = (left + right) // 2
        start = calc_start(mid)
        if start <= N:
            left = mid
        else:
            right = mid

    ans = ''
    for i in range(left, left + 30):
        tmp = ''
        if i % 3 == 0:
            tmp += 'Fizz'
        if i % 5 == 0:
            tmp += 'Buzz'
        if not tmp:
            tmp = str(i)
        ans += tmp

    start = calc_start(left)
    return ans[N - start:N - start + 20]