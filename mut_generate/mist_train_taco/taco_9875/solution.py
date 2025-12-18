"""
QUESTION:
Problem statement

Of the string set $ S $ that meets the following conditions, configure $ 1 $ with the largest number of elements.

* The length of the string contained in $ S $ is $ 1 $ or more and $ N $ or less.
* The lengths of the strings contained in $ S $ are different.
* The string contained in $ S $ consists only of the characters `0` and` 1`.
* For any $ 2 $ string contained in $ S $, one is not a substring of the other.



However, the substring of the string $ x $ is the string obtained by removing more than $ 0 $ characters from the beginning and end of $ x $.

Constraint

* $ 1 \ leq N \ leq 300 $
* $ N $ is an integer



* * *

input

Input is given from standard input in the following format.


$ N $


output

Output $ 1 $ of the string set $ S $ that satisfies the condition with the maximum number of elements. There may be multiple such $ S $, but any output will be correct.

Specifically, output in the following format.

Output $ K $, the number of elements of $ S $, on the $ 1 $ line.

Output all $ S $ elements from the $ 2 $ line to the $ K + 1 $ line. Print $ 1 $ of $ S $ elements on each line.


$ K $
$ S_1 $
$ S_2 $
$ \ vdots $
$ S_K $


* * *

Input example 1


2


Output example 1


2
0
11


The string set $ \\ {0, 11 \\} $ is the set with the largest number of elements that meets the conditions.

* * *

Input example 2


1


Output example 2


1
0






Example

Input

2


Output

2
0
11
"""

def generate_max_string_set(N):
    if N == 1:
        return 1, ["0"]
    elif N == 2:
        return 2, ["0", "11"]
    else:
        S = []
        for i in range(N - 1):
            S.append('0' + '1' * i + '0')
        return N - 1, S