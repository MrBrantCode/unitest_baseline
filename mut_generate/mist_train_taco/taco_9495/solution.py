"""
QUESTION:
Reforms continue entering Berland. For example, during yesterday sitting the Berland Parliament approved as much as n laws (each law has been assigned a unique number from 1 to n). Today all these laws were put on the table of the President of Berland, G.W. Boosch, to be signed.

This time mr. Boosch plans to sign 2k laws. He decided to choose exactly two non-intersecting segments of integers from 1 to n of length k and sign all laws, whose numbers fall into these segments. More formally, mr. Boosch is going to choose two integers a, b (1 ≤ a ≤ b ≤ n - k + 1, b - a ≥ k) and sign all laws with numbers lying in the segments [a; a + k - 1] and [b; b + k - 1] (borders are included).

As mr. Boosch chooses the laws to sign, he of course considers the public opinion. Allberland Public Opinion Study Centre (APOSC) conducted opinion polls among the citizens, processed the results into a report and gave it to the president. The report contains the absurdity value for each law, in the public opinion. As mr. Boosch is a real patriot, he is keen on signing the laws with the maximum total absurdity. Help him.


-----Input-----

The first line contains two integers n and k (2 ≤ n ≤ 2·10^5, 0 < 2k ≤ n) — the number of laws accepted by the parliament and the length of one segment in the law list, correspondingly. The next line contains n integers x_1, x_2, ..., x_{n} — the absurdity of each law (1 ≤ x_{i} ≤ 10^9).


-----Output-----

Print two integers a, b — the beginning of segments that mr. Boosch should choose. That means that the president signs laws with numbers from segments [a; a + k - 1] and [b; b + k - 1]. If there are multiple solutions, print the one with the minimum number a. If there still are multiple solutions, print the one with the minimum b.


-----Examples-----
Input
5 2
3 6 1 1 6

Output
1 4

Input
6 2
1 1 1 1 1 1

Output
1 3



-----Note-----

In the first sample mr. Boosch signs laws with numbers from segments [1;2] and [4;5]. The total absurdity of the signed laws equals 3 + 6 + 1 + 6 = 16.

In the second sample mr. Boosch signs laws with numbers from segments [1;2] and [3;4]. The total absurdity of the signed laws equals 1 + 1 + 1 + 1 = 4.
"""

def find_optimal_segments(n, k, absurdity_values):
    # Calculate the sum of the first segment
    s = [sum(absurdity_values[0:k])]
    m = [0]
    sm = [s[-1]]
    
    # Calculate the sum of each segment and keep track of the maximum sum segment
    for i in range(1, n - k + 1):
        s.append(s[-1] + absurdity_values[i + k - 1] - absurdity_values[i - 1])
        if s[-1] > sm[-1]:
            m.append(i)
            sm.append(s[-1])
        else:
            m.append(m[-1])
            sm.append(sm[-1])
    
    # Find the optimal segments
    a, b = 0, k
    sms = sm[0] + s[k]
    for i in range(k + 1, n - k + 1):
        if sm[i - k] + s[i] > sms:
            sms = sm[i - k] + s[i]
            a = m[i - k]
            b = i
    
    # Return the 1-based indices
    return (a + 1, b + 1)