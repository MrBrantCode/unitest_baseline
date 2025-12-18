"""
QUESTION:
What are you doing at the end of the world? Are you busy? Will you save us?



[Image]

Nephren is playing a game with little leprechauns.

She gives them an infinite array of strings, f_{0... ∞}.

f_0 is "What are you doing at the end of the world? Are you busy? Will you save us?".

She wants to let more people know about it, so she defines f_{i} =  "What are you doing while sending "f_{i} - 1"? Are you busy? Will you send "f_{i} - 1"?" for all i ≥ 1.

For example, f_1 is

"What are you doing while sending "What are you doing at the end of the world? Are you busy? Will you save us?"? Are you busy? Will you send "What are you doing at the end of the world? Are you busy? Will you save us?"?". Note that the quotes in the very beginning and in the very end are for clarity and are not a part of f_1.

It can be seen that the characters in f_{i} are letters, question marks, (possibly) quotation marks and spaces.

Nephren will ask the little leprechauns q times. Each time she will let them find the k-th character of f_{n}. The characters are indexed starting from 1. If f_{n} consists of less than k characters, output '.' (without quotes).

Can you answer her queries?


-----Input-----

The first line contains one integer q (1 ≤ q ≤ 10) — the number of Nephren's questions.

Each of the next q lines describes Nephren's question and contains two integers n and k (0 ≤ n ≤ 10^5, 1 ≤ k ≤ 10^18).


-----Output-----

One line containing q characters. The i-th character in it should be the answer for the i-th query.


-----Examples-----
Input
3
1 1
1 2
1 111111111111

Output
Wh.
Input
5
0 69
1 194
1 139
0 47
1 66

Output
abdef
Input
10
4 1825
3 75
3 530
4 1829
4 1651
3 187
4 584
4 255
4 774
2 474

Output
Areyoubusy


-----Note-----

For the first two examples, refer to f_0 and f_1 given in the legend.
"""

def find_character_in_sequence(n: int, k: int) -> str:
    f0 = 'What are you doing at the end of the world? Are you busy? Will you save us?'
    first_part = 'What are you doing while sending "'
    between1 = '"? Are you busy? Will you send "'
    
    # Precompute lengths of f_i for i up to 64
    f_lengths = [0 for _ in range(64)]
    f_lengths[0] = len(f0)
    for i in range(1, 64):
        f_lengths[i] = 2 * f_lengths[i - 1] + 68
    
    def determine_n(n, k):
        while n > 64 and k >= 34:
            k -= 34
            n -= 1
        return n
    
    def index_find(n, k) -> str:
        if n == 0:
            if k >= len(f0):
                return '.'
            return f0[k]
        if k < 34:
            return first_part[k]
        first_end = 34 + f_lengths[n - 1]
        if 34 <= k < first_end:
            return index_find(n - 1, k - 34)
        if first_end <= k < first_end + 32:
            return between1[k - first_end]
        second_end = f_lengths[n - 1] + first_end + 32
        if first_end + 32 <= k < second_end:
            return index_find(n - 1, k - first_end - 32)
        else:
            if k - second_end > 1:
                return '.'
            return '"?'[k - second_end]
    
    if n > 64:
        new_n = determine_n(n, k - 1)
        prefix = (n - new_n) * 34
        return index_find(new_n, k - 1 - prefix)
    else:
        return index_find(n, k - 1)