"""
QUESTION:
Divya's watch of worth Rs10 cr is abducted by N thieves(1,2....i...N). The fight over the watch leads to a final decision that it should belong to the thief who wins a simple game. The rules of the game state that every thief  registers a time in the format HH:MM:SS . Accordingly the average A of three clockwise angles  between the hours , minutes and seconds hands is calculated . Thus the ith thief  with the maximum A wins the game and gets to keep the watch.

The thieves are poor in mathematics and will need your help . Given the number of thieves and their registered time resolves the conflict and help them in choosing the winner 

-----Input-----
First line of input contains T which denotes the number of test cases.

The first line of each test case consists of an integer which denotes the number of thieves thereby N line follow which give the time choosen by each thieve in the format HH:MM:SS.

-----Output:-----
Output single integer i which denotes the ith thief.

-----Constraints:-----

1<=T<=100

1<=N<=50

01<=HH<=12

00<=MM<=60

00<=SS<=60

-----Example:-----
Input:
2
3
12:28:26
07:26:04
11:23:17
2
07:43:25
06:23:34

Output:
3
1
"""

def find_winning_thief(test_cases):
    def calculate_average_angle(h, m, s):
        h %= 12
        m %= 60
        s %= 60
        ha = h * 30 + m * 0.5 + s * 0.5 / 60
        ma = m * 6 + s * 0.1
        sa = s * 6
        hm1 = abs(ha - ma)
        hm2 = 360 - hm1
        hm3 = abs(hm1 - hm2)
        hm = min(hm1, hm2, hm3)
        ms1 = abs(ma - sa)
        ms2 = 360 - ms1
        ms3 = abs(ms1 - ms2)
        ms = min(ms1, ms2, ms3)
        sh1 = abs(sa - ha)
        sh2 = 360 - sh1
        sh3 = abs(sh1 - sh2)
        sh = min(sh1, sh2, sh3)
        avg = (hm + ms + sh) / 3
        return avg

    results = []
    for thieves_times in test_cases:
        mx = -1
        for i, time in enumerate(thieves_times):
            h, m, s = map(int, time.split(':'))
            avg = calculate_average_angle(h, m, s)
            if mx < avg:
                ans = i + 1
                mx = avg
        results.append(ans)
    return results