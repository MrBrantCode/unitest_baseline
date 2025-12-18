"""
QUESTION:
Anmol gained a lot of weight last semester. So this semester, he decided to run everyday. There is a very long straight road starting at his hostel. There are N poles on the road - P1, P2, P3,..., PN on the road. All the poles lie on the same side of his hostel. The distance between Pi and his hostel is Di.
For 1 ≤ i, j ≤ N, i < j implies Di < Dj
Everyday, Anmol chooses a pole Pi to start running from. He keeps on running until he reaches Pi+K. Whenever he reaches a pole (other than the starting pole), he records the distance traveled since the last pole.

You are given the distances recorded by him today. Your task is to find the number of distinct values of i such that i + K ≤ N and if he starts at Pi and end at Pi+K, he would end up having exactly the same record of distances (in the same order).

-----Input-----
- The first line of the input contains an integer T denoting the number of test cases.
- The first line of each test case contains two space separated integers N and K.
- The next line contains N space separated integers D1, D2,..., DN.
- The next line contains K space separated integers representing the distances recorded by Anmol in the same order.
.

-----Output-----
- For each test case, output a single line containing the answer for that test case.

-----Constraints-----
- 1 ≤ T ≤ 10
- 2 ≤ N ≤ 5 x 104
- 1 ≤ K < N
- 1 ≤ Di ≤ 106

-----Subtasks-----

-----Subtask #1 (20 points)-----
- 1 ≤ N ≤ 1000

-----Subtask #2 (80 points)-----
- Original constraints

-----Example-----
Input:
3
5 1
1 5 10 12 14
5
5 2
5 8 13 16 21
3 5
5 3
2 6 8 11 16
2 3 5

Output:
1
2
1

-----Explanation-----
Example case 1. If he runs from P2 to P3, he will record (5)
Example case 2. He can start at P1 or P3
Example case 3. He can start at P2
"""

def count_matching_runs(n, k, distances, recorded_distances):
    def KMPMatch(pattern, string):
        M = len(pattern)
        N = len(string)
        ans = 0
        lps = [0] * M
        j = 0
        LPSCompute(pattern, M, lps)
        i = 0
        while i < N:
            if pattern[j] == string[i]:
                i += 1
                j += 1
            if j == M:
                ans += 1
                j = lps[j - 1]
            elif i < N and pattern[j] != string[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return ans

    def LPSCompute(pattern, M, lps):
        len = 0
        lps[0] = 0
        i = 1
        while i < M:
            if pattern[i] == pattern[len]:
                len += 1
                lps[i] = len
                i += 1
            elif len != 0:
                len = lps[len - 1]
            else:
                lps[i] = 0
                i += 1

    string = []
    for i in range(n - 1):
        string.append(distances[i + 1] - distances[i])
    
    return KMPMatch(recorded_distances, string)