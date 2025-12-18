"""
QUESTION:
A sequence of square brackets is regular if by inserting symbols "+" and "1" into it, you can get a regular mathematical expression from it. For example, sequences "[[]][]", "[]" and "[[][[]]]" — are regular, at the same time "][", "[[]" and "[[]]][" — are irregular. 

Draw the given sequence using a minimalistic pseudographics in the strip of the lowest possible height — use symbols '+', '-' and '|'. For example, the sequence "[[][]][]" should be represented as: 

+-        -++- -+    

|+- -++- -+||   |

||   ||   |||   |

|+- -++- -+||   |

+-        -++- -+



Each bracket should be represented with the hepl of one or more symbols '|' (the vertical part) and symbols '+' and '-' as on the example which is given above.

Brackets should be drawn without spaces one by one, only dividing pairs of consecutive pairwise brackets with a single-space bar (so that the two brackets do not visually merge into one symbol). The image should have the minimum possible height. 

The enclosed bracket is always smaller than the surrounding bracket, but each bracket separately strives to maximize the height of the image. So the pair of final brackets in the example above occupies the entire height of the image.

Study carefully the examples below, they adequately explain the condition of the problem. Pay attention that in this problem the answer (the image) is unique. 


-----Input-----

The first line contains an even integer n (2 ≤ n ≤ 100) — the length of the sequence of brackets.

The second line contains the sequence of brackets — these are n symbols "[" and "]". It is guaranteed that the given sequence of brackets is regular. 


-----Output-----

Print the drawn bracket sequence in the format which is given in the condition. Don't print extra (unnecessary) spaces. 


-----Examples-----
Input
8
[[][]][]

Output
+-        -++- -+
|+- -++- -+||   |
||   ||   |||   |
|+- -++- -+||   |
+-        -++- -+

Input
6
[[[]]]

Output
+-     -+
|+-   -+|
||+- -+||
|||   |||
||+- -+||
|+-   -+|
+-     -+

Input
6
[[][]]

Output
+-        -+
|+- -++- -+|
||   ||   ||
|+- -++- -+|
+-        -+

Input
2
[]

Output
+- -+
|   |
+- -+

Input
4
[][]

Output
+- -++- -+
|   ||   |
+- -++- -+
"""

def draw_bracket_sequence(n, brackets):
    levels = [None] * n
    i = 0
    while i < n:
        if brackets[i] == '[':
            level = 0
            levels[i] = level
            for j in range(i + 1, n):
                if brackets[j] == '[':
                    level += 1
                    levels[j] = level
                else:
                    levels[j] = level
                    if level == 0:
                        i = j + 1
                        break
                    level -= 1

    max_level = max(levels)
    len_rotate = n + brackets.count('[]') * 3
    len_rotate_ele = max_level * 2 + 1 + 2
    rotate = [None] * len_rotate
    offset = 0

    for i in range(n):
        cur_level = levels[i]
        cur_index = i + offset
        body_len = (max_level - cur_level) * 2 + 1
        body = ''.join(['+', '|' * body_len, '+'])
        if cur_level == 0:
            rotate[cur_index] = body
        elif cur_level > levels[i - 1] or cur_level > levels[i + 1]:
            space = ' ' * (cur_level - 1)
            rotate[cur_index] = '-'.join([space, body, space])
        else:
            space = ' ' * cur_level
            rotate[cur_index] = ''.join([space, body, space])
        if brackets[i] == '[' and brackets[i + 1] == ']':
            space = ' ' * cur_level
            rotate[cur_index + 1] = rotate[cur_index + 3] = '-'.join([space, ' ' * body_len, space])
            rotate[cur_index + 2] = ' ' * len_rotate_ele
            offset += 3

    rotate_back = [None] * len_rotate_ele
    for i in range(len_rotate_ele):
        line = ''
        for j in range(len_rotate):
            line += rotate[j][i]
        rotate_back[i] = line

    return rotate_back