"""
QUESTION:
Problem Statement

We found a dictionary of the Ancient Civilization Mayo (ACM) during excavation of the ruins. After analysis of the dictionary, we revealed they used a language that had not more than 26 letters. So one of us mapped each letter to a different English alphabet and typed all the words in the dictionary into a computer.

How the words are ordered in the dictionary, especially whether they are ordered lexicographically, is an interesting topic to many people. As a good programmer, you are requested to write a program to judge whether we can consider the words to be sorted in a lexicographical order.

Note: In a lexicographical order, a word always precedes other words it is a prefix of. For example, `ab` precedes `abc`, `abde`, and so on.



Input

The input consists of multiple datasets. Each dataset is formatted as follows:


n
string_1
...
string_n


Each dataset consists of n+1 lines. The first line of each dataset contains an integer that indicates n (1 \leq n \leq 500). The i-th line of the following n lines contains string_i, which consists of up to 10 English lowercase letters.

The end of the input is `0`, and this should not be processed.

Output

Print either `yes` or `no` in a line for each dataset, in the order of the input. If all words in the dataset can be considered to be ordered lexicographically, print `yes`. Otherwise, print `no`.

Example

Input

4
cba
cab
b
a
3
bca
ab
a
5
abc
acb
b
c
c
5
abc
acb
c
b
b
0


Output

yes
no
yes
no
"""

def is_lexicographically_sorted(n, words):
    def add_edge(node, adj_lst, s1, s2):
        ind = 0
        max_len = min(len(s1), len(s2))
        while ind < max_len and s1[ind] == s2[ind]:
            ind += 1
        if ind == max_len:
            return max_len < len(s1)
        c1 = ord(s1[ind]) - ord('a')
        c2 = ord(s2[ind]) - ord('a')
        adj_lst[c1].add(c2)
        node.add(c1)
        node.add(c2)
        return False

    def visit(n, visited, adj_lst):
        ret = False
        if visited[n] == 2:
            return True
        elif visited[n] == 0:
            visited[n] = 2
            for to in adj_lst[n]:
                ret = ret or visit(to, visited, adj_lst)
            visited[n] = 1
        return ret

    node = set()
    adj_lst = [set() for _ in range(26)]
    blank_flag = False
    for i in range(n):
        for j in range(i + 1, n):
            blank_flag = blank_flag or add_edge(node, adj_lst, words[i], words[j])
    if blank_flag:
        return False
    visited = [0] * 26
    cycle_flag = False
    for n in node:
        cycle_flag = cycle_flag or visit(n, visited, adj_lst)
    return not cycle_flag