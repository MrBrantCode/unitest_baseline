"""
QUESTION:
Increasing E869120 (Ninja E869120)

E869120 You are good at alter ego.

Here are $ N $ members of the PA Lab. But some of them may be E869120.

So you asked all the $ N $ members of the PA Lab for their names. As a result, the $ N $ members named themselves $ S_1, S_2, S_3, \ dots, S_N $, respectively.

E869120 How many people did you split into? However, all members of the PA Lab shall honestly answer their names.

input

Input is given from standard input in the following format.


$ N $
$ S_1 $
$ S_2 $
$ S_3 $
$ \ ldots $
$ S_N $


output

E869120 Please output the number of people you were split into. However, if you do not have E869120, please output "0".

However, insert a line break at the end.

Constraint

* $ 1 \ leq N \ leq 1000 $
* $ 1 \ leq (length of S_i $ $) \ leq 100 $
* $ N $ is an integer.
* $ S_i $ is a string consisting of numbers and uppercase letters.



Input example 1


Five
E869120
TMJN
E869120
TAISA
YNYMXIAOLONGBAO


Output example 1


2


E869120 You are split into two.

Input example 2


3
SQUARE1001
MENCOTTON
B2563125


Output example 2


0


E869120 Please output 0 when you are not there.

Input example 3


6
E8691200
E869121
E869122
E869123
E869124
E869125


Output example 3


0


Beware of impostors.





Example

Input

5
E869120
TMJN
E869120
TAISA
YNYMXIAOLONGBAO


Output

2
"""

def count_e869120_occurrences(names):
    """
    Counts the number of times "E869120" appears in the list of names.

    Parameters:
    names (list of str): A list of names.

    Returns:
    int: The number of times "E869120" appears in the list.
    """
    return names.count('E869120')