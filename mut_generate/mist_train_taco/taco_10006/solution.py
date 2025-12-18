"""
QUESTION:
The DNA sequence for every living creature in Berland can be represented as a non-empty line consisting of lowercase Latin letters. Berland scientists found out that all the creatures evolve by stages. During one stage exactly one symbol of the DNA line is replaced by exactly two other ones. At that overall there are n permissible substitutions. The substitution ai->bici means that any one symbol ai can be replaced with two symbols bici. Every substitution could happen an unlimited number of times.

They say that two creatures with DNA sequences s1 and s2 can have a common ancestor if there exists such a DNA sequence s3 that throughout evolution it can result in s1 and s2, perhaps after a different number of stages. Your task is to find out by the given s1 and s2 whether the creatures possessing such DNA sequences can have a common ancestor. If the answer is positive, you have to find the length of the shortest sequence of the common ancestor’s DNA.

Input

The first line contains a non-empty DNA sequence s1, the second line contains a non-empty DNA sequence s2. The lengths of these lines do not exceed 50, the lines contain only lowercase Latin letters. The third line contains an integer n (0 ≤ n ≤ 50) — the number of permissible substitutions. Then follow n lines each of which describes a substitution in the format ai->bici. The characters ai, bi, and ci are lowercase Latin letters. Lines s1 and s2 can coincide, the list of substitutions can contain similar substitutions.

Output

If s1 and s2 cannot have a common ancestor, print -1. Otherwise print the length of the shortest sequence s3, from which s1 and s2 could have evolved.

Examples

Input

ababa
aba
2
c-&gt;ba
c-&gt;cc


Output

2


Input

ababa
aba
7
c-&gt;ba
c-&gt;cc
e-&gt;ab
z-&gt;ea
b-&gt;ba
d-&gt;dd
d-&gt;ab


Output

1


Input

ababa
aba
1
c-&gt;ba


Output

-1
"""

import itertools
import collections

def find_shortest_common_ancestor(s1, s2, substitutions):
    rules = collections.defaultdict(set)
    for source, target in substitutions:
        rules[target].add(source)

    def substrings_of_precise_length(s, l):
        for start_pos in range(len(s) - l + 1):
            yield s[start_pos:start_pos + l]

    def substrings_of_minimum_length(s, minlen):
        return itertools.chain.from_iterable((substrings_of_precise_length(s, l) for l in range(minlen, len(s) + 1)))

    def partitions_of_string(s):
        for l1 in range(1, len(s)):
            yield (s[:l1], s[l1:])

    ancestors = collections.defaultdict(set)

    def update_ancestors(ancestors, rules, s):
        for c in s:
            ancestors[c].add(c)
        for sub in substrings_of_minimum_length(s, 2):
            for (sub1, sub2) in partitions_of_string(sub):
                for target, sources in rules.items():
                    if target[0] in ancestors[sub1] and target[1] in ancestors[sub2]:
                        ancestors[sub].update(sources)

    update_ancestors(ancestors, rules, s1)
    update_ancestors(ancestors, rules, s2)

    def prefixes(s):
        for l in range(1, len(s) + 1):
            yield s[:l]

    def determine_shortest_common_ancestor(ancestors, s1, s2):
        shortest_common_ancestor = collections.defaultdict(lambda: float('inf'))
        for (pre1, pre2) in itertools.product(prefixes(s1), prefixes(s2)):
            if not ancestors[pre1].isdisjoint(ancestors[pre2]):
                shortest_common_ancestor[pre1, pre2] = 1
            temp = shortest_common_ancestor[pre1, pre2]
            for ((sub1a, sub1b), (sub2a, sub2b)) in itertools.product(partitions_of_string(pre1), partitions_of_string(pre2)):
                if not ancestors[sub1b].isdisjoint(ancestors[sub2b]):
                    temp = min(temp, shortest_common_ancestor[sub1a, sub2a] + 1)
            shortest_common_ancestor[pre1, pre2] = temp
        return shortest_common_ancestor[s1, s2]

    answer = determine_shortest_common_ancestor(ancestors, s1, s2)
    return answer if answer != float('inf') else -1