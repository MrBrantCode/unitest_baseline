"""
QUESTION:
Professor GukiZ doesn't accept string as they are. He likes to swap some letters in string to obtain a new one.

GukiZ has strings a, b, and c. He wants to obtain string k by swapping some letters in a, so that k should contain as many non-overlapping substrings equal either to b or c as possible. Substring of string x is a string formed by consecutive segment of characters from x. Two substrings of string x overlap if there is position i in string x occupied by both of them.

GukiZ was disappointed because none of his students managed to solve the problem. Can you help them and find one of possible strings k?

Input

The first line contains string a, the second line contains string b, and the third line contains string c (1 ≤ |a|, |b|, |c| ≤ 105, where |s| denotes the length of string s).

All three strings consist only of lowercase English letters. 

It is possible that b and c coincide.

Output

Find one of possible strings k, as described in the problem statement. If there are multiple possible answers, print any of them.

Examples

Input

aaa
a
b


Output

aaa

Input

pozdravstaklenidodiri
niste
dobri


Output

nisteaadddiiklooprrvz

Input

abbbaaccca
ab
aca


Output

ababacabcc

Note

In the third sample, this optimal solutions has three non-overlaping substrings equal to either b or c on positions 1 – 2 (ab), 3 – 4 (ab), 5 – 7 (aca). In this sample, there exist many other optimal solutions, one of them would be acaababbcc.
"""

from collections import defaultdict

def find_max_possible_substring(a, a_char_counts, char_counts):
    max_count_of_sub = len(a)
    for (char, count) in char_counts.items():
        max_count_of_sub = min(max_count_of_sub, a_char_counts[char] // char_counts[char])
    return max_count_of_sub

def get_optimal_count(a, a_orig_char_counts, max_count_of_first, first_char_counts, second_char_counts):
    max_val = 0
    count_of_first = 0
    count_of_second = 0
    for i in range(max_count_of_first + 1):
        a_char_counts = a_orig_char_counts.copy()
        for (char, count) in first_char_counts.items():
            a_char_counts[char] -= count * i
        remaining_count_of_second = find_max_possible_substring(a, a_char_counts, second_char_counts)
        count = remaining_count_of_second + i
        if max_val < count:
            max_val = count
            count_of_first = i
            count_of_second = remaining_count_of_second
    return (count_of_first, count_of_second)

def get_result(a, a_char_counts, first, max_count_of_first, first_char_counts, second, second_char_counts):
    (optimal_count_of_first, optimal_count_of_second) = get_optimal_count(a, a_char_counts, max_count_of_first, first_char_counts, second_char_counts)
    result = ''
    result += first * optimal_count_of_first
    for (char, count) in first_char_counts.items():
        a_char_counts[char] -= count * optimal_count_of_first
    if optimal_count_of_second:
        result += second * optimal_count_of_second
        for (char, count) in second_char_counts.items():
            a_char_counts[char] -= count * optimal_count_of_second
    for (char, count) in a_char_counts.items():
        result += char * count
    return result

def find_optimal_string(a, b, c):
    a_char_counts = defaultdict(lambda: 0)
    b_char_counts = defaultdict(lambda: 0)
    c_char_counts = defaultdict(lambda: 0)
    
    for char in a:
        a_char_counts[char] += 1
    for char in b:
        b_char_counts[char] += 1
    for char in c:
        c_char_counts[char] += 1
    
    max_count_of_b = find_max_possible_substring(a, a_char_counts, b_char_counts)
    max_count_of_c = find_max_possible_substring(a, a_char_counts, c_char_counts)
    
    if max_count_of_b >= max_count_of_c:
        result = get_result(a, a_char_counts, b, max_count_of_b, b_char_counts, c, c_char_counts)
    else:
        result = get_result(a, a_char_counts, c, max_count_of_c, c_char_counts, b, b_char_counts)
    
    return result