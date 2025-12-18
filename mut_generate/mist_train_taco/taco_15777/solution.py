"""
QUESTION:
You are given a non-empty string s=s_1s_2... s_n, which consists only of lowercase Latin letters. Polycarp does not like a string if it contains at least one string "one" or at least one string "two" (or both at the same time) as a substring. In other words, Polycarp does not like the string s if there is an integer j (1 ≤ j ≤ n-2), that s_{j}s_{j+1}s_{j+2}="one" or s_{j}s_{j+1}s_{j+2}="two".

For example:

  * Polycarp does not like strings "oneee", "ontwow", "twone" and "oneonetwo" (they all have at least one substring "one" or "two"), 
  * Polycarp likes strings "oonnee", "twwwo" and "twnoe" (they have no substrings "one" and "two"). 



Polycarp wants to select a certain set of indices (positions) and remove all letters on these positions. All removals are made at the same time.

For example, if the string looks like s="onetwone", then if Polycarp selects two indices 3 and 6, then "onetwone" will be selected and the result is "ontwne".

What is the minimum number of indices (positions) that Polycarp needs to select to make the string liked? What should these positions be?

Input

The first line of the input contains an integer t (1 ≤ t ≤ 10^4) — the number of test cases in the input. Next, the test cases are given.

Each test case consists of one non-empty string s. Its length does not exceed 1.5⋅10^5. The string s consists only of lowercase Latin letters.

It is guaranteed that the sum of lengths of all lines for all input data in the test does not exceed 1.5⋅10^6.

Output

Print an answer for each test case in the input in order of their appearance.

The first line of each answer should contain r (0 ≤ r ≤ |s|) — the required minimum number of positions to be removed, where |s| is the length of the given line. The second line of each answer should contain r different integers — the indices themselves for removal in any order. Indices are numbered from left to right from 1 to the length of the string. If r=0, then the second line can be skipped (or you can print empty). If there are several answers, print any of them.

Examples

Input


4
onetwone
testme
oneoneone
twotwo


Output


2
6 3
0

3
4 1 7 
2
1 4


Input


10
onetwonetwooneooonetwooo
two
one
twooooo
ttttwo
ttwwoo
ooone
onnne
oneeeee
oneeeeeeetwooooo


Output


6
18 11 12 1 6 21 
1
1 
1
3 
1
2 
1
6 
0

1
4 
0

1
1 
2
1 11 

Note

In the first example, answers are:

  * "onetwone", 
  * "testme" — Polycarp likes it, there is nothing to remove, 
  * "oneoneone", 
  * "twotwo". 



In the second example, answers are: 

  * "onetwonetwooneooonetwooo", 
  * "two", 
  * "one", 
  * "twooooo", 
  * "ttttwo", 
  * "ttwwoo" — Polycarp likes it, there is nothing to remove, 
  * "ooone", 
  * "onnne" — Polycarp likes it, there is nothing to remove, 
  * "oneeeee", 
  * "oneeeeeeetwooooo".
"""

def find_indices_to_remove(s: str) -> (int, list):
    R = []
    i = 0
    while i < len(s):
        if i + 4 < len(s) and s[i:i + 5] == 'twone':
            R.append(i + 2 + 1)  # Append the index of 'o' in 'twone'
            i += 5
        elif i + 2 < len(s) and (s[i:i + 3] == 'one' or s[i:i + 3] == 'two'):
            R.append(i + 1 + 1)  # Append the index of the middle character in 'one' or 'two'
            i += 3
        else:
            i += 1
    return len(R), R