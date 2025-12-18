"""
QUESTION:
If you visit Aizu Akabeko shrine, you will find a unique paper fortune on which a number with more than one digit is written.

Each digit ranges from 1 to 9 (zero is avoided because it is considered a bad omen in this shrine). Using this string of numeric values, you can predict how many years it will take before your dream comes true. Cut up the string into more than one segment and compare their values. The difference between the largest and smallest value will give you the number of years before your wish will be fulfilled. Therefore, the result varies depending on the way you cut up the string. For example, if you are given a string 11121314 and divide it into segments, say, as 1,11,21,3,14, then the difference between the largest and smallest is 21 - 1 = 20. Another division 11,12,13,14 produces 3 (i.e. 14 - 11) years. Any random division produces a game of luck. However, you can search the minimum number of years using a program.

Given a string of numerical characters, write a program to search the minimum years before your wish will be fulfilled.



Input

The input is given in the following format.


n


An integer n is given. Its number of digits is from 2 to 100,000, and each digit ranges from 1 to 9.

Output

Output the minimum number of years before your wish will be fulfilled.

Examples

Input

11121314


Output

3


Input

123125129


Output

6


Input

119138


Output

5
"""

def calculate_minimum_years(n: str) -> int:
    def sub(maxs, mins):
        for i in range(len(maxs)):
            if maxs[i] != mins[i]:
                if i == len(maxs) - 1:
                    return int(maxs[i]) - int(mins[i])
                if i == len(maxs) - 2:
                    return int(maxs[i:i + 2]) - int(mins[i:i + 2])
                return 10
        return 0

    def checkEqual(S):
        ans = 8
        for k in range(1, len(S)):
            if len(S) % k != 0:
                continue
            mins = maxs = S[0:k]
            for s in range(0, len(S), k):
                maxs = max(maxs, S[s:s + k])
                mins = min(mins, S[s:s + k])
            ans = min(ans, sub(maxs, mins))
        return ans

    def check12(S):
        maxv = 0
        minv = 10
        p = 0
        while p < len(S):
            v = int(S[p])
            if S[p] == '1' and p + 1 < len(S):
                v = 10 + int(S[p + 1])
                p += 1
            maxv = max(maxv, v)
            minv = min(minv, v)
            p += 1
        return maxv - minv

    return min(checkEqual(n), check12(n))