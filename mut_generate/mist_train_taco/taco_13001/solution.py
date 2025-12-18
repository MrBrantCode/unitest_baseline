"""
QUESTION:
Do you know "sed," a tool provided with Unix? Its most popular use is to substitute every occurrence of a string  contained in the input string (actually each input line) with another string β. More precisely, it proceeds as follows.

1. Within the input string, every non-overlapping (but possibly adjacent) occurrences of α are marked. If there is more than one possibility for non-overlapping matching, the leftmost one is chosen.
2. Each of the marked occurrences is substituted with β to obtain the output string; other parts of the input string remain intact.



For example, when α is "aa" and β is "bca", an input string "aaxaaa" will produce "bcaxbcaa", but not "aaxbcaa" nor "bcaxabca". Further application of the same substitution to the string "bcaxbcaa" will result in "bcaxbcbca", but this is another substitution, which is counted as the second one.

In this problem, a set of substitution pairs (αi, βi) (i = 1, 2, ... , n), an initial string γ, and a final string δ are given, and you must investigate how to produce δ from γ with a minimum number of substitutions. A single substitution (αi, βi) here means simultaneously substituting all the non-overlapping occurrences of αi, in the sense described above, with βi.

You may use a specific substitution (αi, βi ) multiple times, including zero times.



Input

The input consists of multiple datasets, each in the following format.

n
α1 β1
α2 β2
.
.
.
αn βn
γ δ

n is a positive integer indicating the number of pairs. αi and βi are separated by a single space. You may assume that 1 ≤ |αi| < |βi| ≤ 10 for any i (|s| means the length of the string s), αi ≠ αj for any i ≠ j, n ≤ 10 and 1 ≤ |γ| < |δ| ≤ 10. All the strings consist solely of lowercase letters. The end of the input is indicated by a line containing a single zero.

Output

For each dataset, output the minimum number of substitutions to obtain δ from γ. If δ cannot be produced from γ with the given set of substitutions, output -1.

Example

Input

2
a bb
b aa
a
bbbbbbbb
1
a aa
a
aaaaa
3
ab aab
abc aadc
ad dee
abc
deeeeeeeec
10
a abc
b bai
c acf
d bed
e abh
f fag
g abe
h bag
i aaj
j bbb
a
abacfaabe
0


Output

3
-1
7
4
"""

def minimum_substitutions(n, substitution_pairs, initial_string, final_string):
    l = len(final_string)
    if initial_string == final_string:
        return 0
    
    visited = set([initial_string])
    current_set = set([initial_string])
    t = 0
    r = -1
    
    while current_set:
        t += 1
        next_set = set()
        for cs in current_set:
            for (α, β) in substitution_pairs:
                nt = cs.replace(α, β)
                if len(nt) > l:
                    continue
                next_set.add(nt)
        
        if final_string in next_set:
            r = t
            break
        
        current_set = next_set - visited
        visited |= next_set
    
    return r