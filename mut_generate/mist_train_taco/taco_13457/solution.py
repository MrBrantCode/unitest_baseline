"""
QUESTION:
zscoder loves simple strings! A string t is called simple if every pair of adjacent characters are distinct. For example ab, aba, zscoder are simple whereas aa, add are not simple.

zscoder is given a string s. He wants to change a minimum number of characters so that the string s becomes simple. Help him with this task!

Input

The only line contains the string s (1 ≤ |s| ≤ 2·105) — the string given to zscoder. The string s consists of only lowercase English letters.

Output

Print the simple string s' — the string s after the minimal number of changes. If there are multiple solutions, you may output any of them.

Note that the string s' should also consist of only lowercase English letters.

Examples

Input

aab


Output

bab


Input

caaab


Output

cabab


Input

zscoder


Output

zscoder
"""

def make_string_simple(s: str) -> str:
    def find_distinct_char(a: str, b: str = None) -> str:
        chars = 'anfrozeyuibiu' if b else 'urweifbn'
        for char in chars:
            if char != a and (not b or char != b):
                return char
        return ''

    s_list = list(s)
    n = len(s_list)

    for i in range(1, n):
        if s_list[i] == s_list[i - 1]:
            if i == n - 1:
                s_list[i] = find_distinct_char(s_list[i])
            else:
                s_list[i] = find_distinct_char(s_list[i], s_list[i + 1])

    return ''.join(s_list)