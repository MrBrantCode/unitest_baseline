"""
QUESTION:
Problem

Given the strings $ s $, $ t $.
First, let the string set $ A = $ {$ s $}, $ B = \ phi $.
At this time, I want to perform the following operations as much as possible.

operation

step1

Perform the following processing for all $ u ∊ A $.

1. From all subsequences of $ u $ (not necessarily contiguous), choose any one that is equal to $ t $. Let the indexes corresponding to $ u $ of the selected subsequence be $ z_1 $, $ z_2 $,…, $ z_ {| t |} $ (however, 1 $ \ le $ $ z_1 $ $ \ lt $ $ z_2). $$ \ lt $… $ \ lt $ $ z_ {| t |} $ $ \ le $ $ | u | $). If there is no such subsequence, the operation ends.


2. Divide the original string with the selected substring characters $ u_ {z_1} $, $ u_ {z_2} $,…, $ u_ {z_ {| t |}} $ and convert them to $ B $ to add.

For example, in the case of $ u = $ "abcdcd" and $ t = $ "ac", the following two division methods can be considered.
If you choose the first and third characters of $ u $, it will be split into "", "b" and "dcd".
If you choose the first and fifth characters of $ u $, it will be split into "", "bcd" and "d".


step2

Replace $ A $ with $ B $ and empty $ B $.
Increase the number of operations by 1.

Subsequence example

The subsequences of "abac" are {"", "a", "b", "c", "aa", "ab", "ac", "ba", "bc", "aac", "aba" "," abc "," bac "," abac "}.
"a" is a subsequence created by extracting the first or third character of "abac".
"ac" is a subsequence created by extracting the 1st and 4th characters of "abac" or the 3rd and 4th characters.

Constraints

The input satisfies the following conditions.

* 1 $ \ le $ $ | t | $ $ \ le $ $ | s | $ $ \ le $ $ 10 ^ 5 $
* Characters contained in the strings $ s $ and $ t $ are uppercase or lowercase letters of the alphabet

Input

The input is given in the following format.


$ s $
$ t $


The string $ s $ is given on the first line, and the string $ t $ is given on the second line.

Output

Output the maximum number of operations.

Examples

Input

AABABCAC
A


Output

2


Input

abaabbabaabaabbabbabaabbab
ab


Output

3


Input

AbCdEfG
aBcDeFg


Output

0
"""

def max_operations(s: str, t: str) -> int:
    t = ' ' + t  # Prepend a space to t for easier indexing
    line = [1]
    next = 1
    t_size = len(t)
    flag = False
    
    for i in s:
        if t[next] == i:
            line[0] += 1
            next = line[0]
            line += [0]
            j = 0
            while line[j] == t_size:
                line[j] = 0
                next = line[j + 1] = line[j + 1] + 1
                j += 1
            if line[-1] == 0:
                line.pop()
    
    return len(line) - 1