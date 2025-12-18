"""
QUESTION:
problem

During this time of winter in Japan, hot days continue in Australia in the Southern Hemisphere. IOI, who lives in Australia, decided to plan what clothes to wear based on the weather forecast for a certain D day. The maximum temperature on day i (1 ≤ i ≤ D) is predicted to be Ti degrees.

IOI has N kinds of clothes, which are numbered from 1 to N. Clothes j (1 ≤ j ≤ N) are suitable for wearing on days when the maximum temperature is above Aj and below Bj. In addition, each clothes has an integer called "flashiness", and the flashiness of clothes j is Cj.

For each of the D days, IOI chooses to wear one of the clothes suitable for wearing when the maximum temperature follows the weather forecast. You may choose the same clothes as many times as you like, or you may choose clothes that are never chosen in D days.

IOI, who wanted to avoid wearing similar clothes in succession, decided to maximize the total absolute value of the difference in the flashiness of the clothes worn on consecutive days. That is, assuming that the clothes xi are selected on the i-day, we want to maximize the values ​​| Cx1 --Cx2 | + | Cx2 --Cx3 | +… + | CxD-1 --CxD |. Create a program to find this maximum value.

input

The input consists of 1 + D + N lines.

On the first line, two integers D and N (2 ≤ D ≤ 200, 1 ≤ N ≤ 200) are written with a blank as a delimiter. D is the number of days to plan clothes and N is the number of clothes types IOI has.

One integer Ti (0 ≤ Ti ≤ 60) is written in the i-th line (1 ≤ i ≤ D) of the following D lines. This means that the maximum temperature on day i is forecast to be Ti degrees.

In the jth line (1 ≤ j ≤ N) of the following N lines, three integers Aj, Bj, Cj (0 ≤ Aj ≤ Bj ≤ 60, 0 ≤ Cj ≤ 100) are written. These indicate that clothing j is suitable for wearing on days when the maximum temperature is above Aj and below Bj, and the flashiness is Cj.

It is guaranteed that there will be at least one piece of clothing suitable for wearing when the maximum temperature follows the weather forecast for every D day.

output

Output the total absolute value of the difference in the flashiness of clothes worn on consecutive days, that is, the maximum value of the values ​​| Cx1 --Cx2 | + | Cx2 --Cx3 | +… + | CxD-1 --CxD | in one line. ..

Input / output example

Input example 1


3 4
31
27
35
20 25 30
23 29 90
21 35 60
28 33 40


Output example 1


80


In the input / output example 1, the candidates for clothes on the first day are clothes 3 and 4, the candidates for clothes on the second day are clothes 2 and clothes 3, and the candidates for clothes on the third day are only clothes 3. is there. Choose clothes 4 on the first day, clothes 2 on the second day, and clothes 3 on the third day. That is, x1 = 4, x2 = 2, x3 = 3. At this time, the absolute value of the difference in the flashiness of the clothes on the first day and the second day is | 40 --90 | = 50, and the absolute value of the difference in the flashiness of the clothes on the second and third days is | 90-60 | = 30. The total is 80, which is the maximum value.

Input example 2


5 2
26
28
32
29
34
30 35 0
25 30 100


Output example 2


300


In Example 2 of input / output, clothes 2 on the first day, clothes 2 on the second day, clothes 1 on the third day, clothes 2 on the fourth day, and clothes 1 on the fifth day. You have to choose. At this time, the required value is | 100 --100 | + | 100 --0 | + | 0 --100 | + | 100 --0 | = 300.

The question text and the data used for the automatic referee are the question text and the test data for scoring, which are created and published by the Japan Committee for Information Olympics.





Example

Input

3 4
31
27
35
20 25 30
23 29 90
21 35 60
28 33 40


Output

80
"""

def maximize_flashiness_difference(D, N, T, clothes):
    clothes.sort(key=lambda x: x[2])
    candidate = []
    for t in T:
        ct = tuple(filter(lambda x: x[0] <= t <= x[1], clothes))
        c_min = ct[0][2]
        c_max = ct[-1][2]
        if c_min == c_max:
            candidate.append((c_min,))
        else:
            candidate.append((c_min, c_max))
    dp = [0] * len(candidate[0])
    for (c1, c2) in zip(candidate, candidate[1:]):
        dp = [max((rec + abs(ci - cj) for (rec, ci) in zip(dp, c1))) for cj in c2]
    return max(dp)