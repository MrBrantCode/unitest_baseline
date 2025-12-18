"""
QUESTION:
You're playing a video game, in which you will get an achievement if you complete all of the levels consecutively without dying. You can play the levels in any order, and each time you play a level you'll either complete it or die. Each level has some probability that you'll complete it, and takes some amount of time. In what order should you play the levels so that the expected time it takes you to get the achievement is minimized? Assume that it takes equally long to beat a level or to die in it, and that you will start again from the first level in your ordering as soon as you die.

Note: If you fail to complete a level, you do not personally die—only your character in the game dies. If that were not the case, only a few people would try to earn this achievement.

Input

The first line of the input gives the number of test cases, T. T test cases follow, each of which consists of three lines. The first line of each test case contains a single integer N, the number of levels. The second line contains N space-separated integers Li. Li is the number of seconds level i lasts, which is independent of whether you complete the level or die. The third line contains N space-separated integers Pi. Pi is the percent chance that you will die in any given attempt to complete level i.

Output

For each test case, output one line containing "Case #x: ", where x is the case number (starting from 1), followed by N space-separated integers. The jth integer in the list should be the index of the jth level you should attempt to beat in order to minimize the amount of time you expect to spend earning the achievement.

Indices go from 0 to N-1. If there are multiple orderings that would give the same expected time, output the lexicographically least ordering. Out of two orderings, the lexicographically smaller one is the one with the smaller index at the first location where they differ; out of many orderings, the lexicographically least one is the one that is lexicographically smaller than every other ordering.

Constraints

1 ≤ T ≤ 100.
0 ≤ Pi < 100.

SAMPLE INPUT
1
4
1 1 1 1
50 0 20 20

SAMPLE OUTPUT
Case #1: 0 2 3 1
"""

def minimize_achievement_time(T, test_cases):
    def sort_list(process_list, n):
        for i in range(1, n):
            key = process_list[i][1]
            temp = process_list[i]
            j = i - 1
            while j >= 0 and process_list[j][1] > key:
                process_list[j + 1] = process_list[j]
                j -= 1
            process_list[j + 1] = temp
        return process_list

    results = []
    
    for case_num, (N, L, P) in enumerate(test_cases, start=1):
        pL = []
        for i in range(N):
            pL.append((i, -P[i]))
        sorted_pL = sort_list(pL, N)
        
        ans = f"Case #{case_num}: "
        for item in sorted_pL:
            ans += str(item[0]) + " "
        results.append(ans.strip())
    
    return results