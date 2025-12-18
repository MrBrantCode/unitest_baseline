"""
QUESTION:
One Martian boy called Zorg wants to present a string of beads to his friend from the Earth — Masha. He knows that Masha likes two colours: blue and red, — and right in the shop where he has come, there is a variety of adornments with beads of these two colours. All the strings of beads have a small fastener, and if one unfastens it, one might notice that all the strings of beads in the shop are of the same length. Because of the peculiarities of the Martian eyesight, if Zorg sees one blue-and-red string of beads first, and then the other with red beads instead of blue ones, and blue — instead of red, he regards these two strings of beads as identical. In other words, Zorg regards as identical not only those strings of beads that can be derived from each other by the string turnover, but as well those that can be derived from each other by a mutual replacement of colours and/or by the string turnover.

It is known that all Martians are very orderly, and if a Martian sees some amount of objects, he tries to put them in good order. Zorg thinks that a red bead is smaller than a blue one. Let's put 0 for a red bead, and 1 — for a blue one. From two strings the Martian puts earlier the string with a red bead in the i-th position, providing that the second string has a blue bead in the i-th position, and the first two beads i - 1 are identical.

At first Zorg unfastens all the strings of beads, and puts them into small heaps so, that in each heap strings are identical, in his opinion. Then he sorts out the heaps and chooses the minimum string in each heap, in his opinion. He gives the unnecassary strings back to the shop assistant and says he doesn't need them any more. Then Zorg sorts out the remaining strings of beads and buys the string with index k. 

All these manupulations will take Zorg a lot of time, that's why he asks you to help and find the string of beads for Masha.

Input

The input file contains two integers n and k (2 ≤ n ≤ 50;1 ≤ k ≤ 1016) —the length of a string of beads, and the index of the string, chosen by Zorg. 

Output

Output the k-th string of beads, putting 0 for a red bead, and 1 — for a blue one. If it s impossible to find the required string, output the only number -1.

Examples

Input

4 4


Output

0101

Note

Let's consider the example of strings of length 4 — 0001, 0010, 0011, 0100, 0101, 0110, 0111, 1000, 1001, 1010, 1011, 1100, 1101, 1110. Zorg will divide them into heaps: {0001, 0111, 1000, 1110}, {0010, 0100, 1011, 1101}, {0011, 1100}, {0101, 1010}, {0110, 1001}. Then he will choose the minimum strings of beads in each heap: 0001, 0010, 0011, 0101, 0110. The forth string — 0101.
"""

def find_kth_bead_string(n, k):
    def calc(lower, upper, record, eq, eq_i):
        if lower > upper:
            return 1
        key = (lower, eq, eq_i)
        if key in record:
            return record[key]
        t = 0
        for x in ['0', '1'] if result[lower] == '?' else [result[lower]]:
            temp = None
            if lower == upper:
                temp = [x]
            elif result[upper] == '?':
                temp = ['0', '1']
            else:
                temp = [result[upper]]
            for y in temp:
                if not (eq and x > y or (eq_i and x == y == '1')):
                    t += calc(lower + 1, upper - 1, record, eq and x == y, eq_i and x != y)
        record[key] = t
        return t

    k += 1
    result = ['?'] * n
    for i in range(n):
        result[i] = '0'
        passed = calc(0, n - 1, {}, True, True)
        if k > passed:
            k -= passed
            result[i] = '1'
    
    if result[0] == '0':
        return ''.join(result)
    else:
        return -1