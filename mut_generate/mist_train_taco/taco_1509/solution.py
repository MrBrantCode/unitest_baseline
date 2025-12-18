"""
QUESTION:
Alice has a string consisting of characters 'A', 'B' and 'C'. Bob can use the following transitions on any substring of our string in any order any number of times:   A $\rightarrow$ BC  B $\rightarrow$ AC  C $\rightarrow$ AB  AAA $\rightarrow$ empty string 

Note that a substring is one or more consecutive characters. For given queries, determine whether it is possible to obtain the target string from source.


-----Input-----

The first line contains a string S (1 ≤ |S| ≤ 10^5). The second line contains a string T (1 ≤ |T| ≤ 10^5), each of these strings consists only of uppercase English letters 'A', 'B' and 'C'.

The third line contains the number of queries Q (1 ≤ Q ≤ 10^5).

The following Q lines describe queries. The i-th of these lines contains four space separated integers a_{i}, b_{i}, c_{i}, d_{i}. These represent the i-th query: is it possible to create T[c_{i}..d_{i}] from S[a_{i}..b_{i}] by applying the above transitions finite amount of times?

Here, U[x..y] is a substring of U that begins at index x (indexed from 1) and ends at index y. In particular, U[1..|U|] is the whole string U.

It is guaranteed that 1 ≤ a ≤ b ≤ |S| and 1 ≤ c ≤ d ≤ |T|.


-----Output-----

Print a string of Q characters, where the i-th character is '1' if the answer to the i-th query is positive, and '0' otherwise.


-----Example-----
Input
AABCCBAAB
ABCB
5
1 3 1 2
2 2 2 4
7 9 1 1
3 4 2 3
4 5 1 3

Output
10011



-----Note-----

In the first query we can achieve the result, for instance, by using transitions $A A B \rightarrow A A A C \rightarrow \operatorname{AAA} A B \rightarrow A B$.

The third query asks for changing AAB to A — but in this case we are not able to get rid of the character 'B'.
"""

def can_transform_strings(s: str, t: str, queries: list) -> str:
    def fast_counter(s):
        a_last, b_count = [0], [0]
        for c in s:
            if c == 'A':
                a_last.append(a_last[-1] + 1)
                b_count.append(b_count[-1])
            else:
                a_last.append(0)
                b_count.append(b_count[-1] + 1)
        return a_last, b_count

    def mask(l, r, info):
        return info[1][r] - info[1][l], min(r - l, info[0][r])

    def can_transform(from_mask, to_mask):
        if from_mask[0] > to_mask[0]:
            return False
        elif (to_mask[0] - from_mask[0]) % 2 != 0:
            return False
        elif to_mask[0] == from_mask[0]:
            if to_mask[1] > from_mask[1]:
                return False
            return (from_mask[1] - to_mask[1]) % 3 == 0
        elif from_mask[0] == 0:
            return to_mask[1] < from_mask[1]
        else:
            return to_mask[1] <= from_mask[1]

    s_info, t_info = fast_counter(s), fast_counter(t)
    answer = ''
    for (l1, r1, l2, r2) in queries:
        l1, l2 = l1 - 1, l2 - 1
        from_mask = mask(l1, r1, s_info)
        to_mask = mask(l2, r2, t_info)
        if can_transform(from_mask, to_mask):
            answer += '1'
        else:
            answer += '0'
    return answer