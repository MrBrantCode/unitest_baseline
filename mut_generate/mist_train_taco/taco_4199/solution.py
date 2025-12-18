"""
QUESTION:
Many countries have such a New Year or Christmas tradition as writing a letter to Santa including a wish list for presents. Vasya is an ordinary programmer boy. Like all ordinary boys, he is going to write the letter to Santa on the New Year Eve (we Russians actually expect Santa for the New Year, not for Christmas). 

Vasya has come up with an algorithm he will follow while writing a letter. First he chooses two strings, s1 anf s2, consisting of uppercase English letters. Then the boy makes string sk, using a recurrent equation sn = sn - 2 + sn - 1, operation '+' means a concatenation (that is, the sequential record) of strings in the given order. Then Vasya writes down string sk on a piece of paper, puts it in the envelope and sends in to Santa. 

Vasya is absolutely sure that Santa will bring him the best present if the resulting string sk has exactly x occurrences of substring AC (the short-cut reminds him оf accepted problems). Besides, Vasya decided that string s1 should have length n, and string s2 should have length m. Vasya hasn't decided anything else.

At the moment Vasya's got urgent New Year business, so he asks you to choose two strings for him, s1 and s2 in the required manner. Help Vasya.

Input

The first line contains four integers k, x, n, m (3 ≤ k ≤ 50; 0 ≤ x ≤ 109; 1 ≤ n, m ≤ 100).

Output

In the first line print string s1, consisting of n uppercase English letters. In the second line print string s2, consisting of m uppercase English letters. If there are multiple valid strings, print any of them.

If the required pair of strings doesn't exist, print "Happy new year!" without the quotes.

Examples

Input

3 2 2 2


Output

AC
AC


Input

3 3 2 2


Output

Happy new year!


Input

3 0 2 2


Output

AA
AA


Input

4 3 2 1


Output

Happy new year!


Input

4 2 2 1


Output

Happy new year!
"""

def find_santa_strings(k, x, n, m):
    def f(s, e, n, cnt):
        ret = [''] * n
        ret[0] = s
        ret[-1] = e
        sa = 0 if s == 'A' else 1
        for i in range(cnt):
            ret[sa] = 'A'
            ret[sa + 1] = 'C'
            sa += 2
        for j in range(sa, n - 1):
            ret[j] = 'B'
        return ''.join(ret)
    
    for sa in 'ABC':
        for ea in 'ABC':
            if n == 1:
                ea = sa
            for sb in 'ABC':
                for eb in 'ABC':
                    if m == 1:
                        eb = sb
                    N = max(0, n - (sa != 'A') - (ea != 'C'))
                    M = max(0, m - (sb != 'A') - (eb != 'C'))
                    for i in range(1 + N // 2):
                        for j in range(1 + M // 2):
                            A = sa + ea
                            B = sb + eb
                            (a, b) = (i, j)
                            for c in range(k - 2):
                                (a, b) = (b, a + b)
                                if A[1] == 'A' and B[0] == 'C':
                                    b += 1
                                (A, B) = (B, A[0] + B[1])
                            if b == x:
                                return (f(sa, ea, n, i), f(sb, eb, m, j))
    return "Happy new year!"