"""
QUESTION:
Sherlock Holmes is bored to death as there aren't any interesting cases to solve. Dr Watson finding it impossible to be around Sherlock goes out to get some fresh air. Just as he lays his feet out of the door, he is thrown right back into his house by the explosion in front of his apartment. The metropolitan police arrive at the scene a few minutes later. They search the place thoroughly for any evidence that could throw some light on the event that unfolded. Unable to get any clues, they call Sherlock for help. After repeated persuasion by Mycroft Holmes and Dr Watson, Sherlock agrees to look at the crime scene. 

Sherlock walks into the apartment, the walls are all black and dripping wet as the fire was recently extinguished. With his skills, he observes, deduces and eliminates the impossible. What's left after it is a simple puzzle left by an evil computer genius and the future Arch Nemesis of Sherlock, Jim Moriarty. 

Given a binary string (S) which contains '0's and '1's and an integer K, 

find the length (L) of the longest contiguous subsequence of (S * K) such that twice the number of zeroes is <= thrice the number of ones (2 * #0s <= 3 * #1s) in that sequence.

S * K is defined as follows:
S * 1 = S 

S * K = S + S * (K - 1)  

Input Format 

The first (and only) line contains an integer K and the binary string S separated by a single space. 

Constraints 

1 <= |S| <= 1,000,000 

1 <=  K  <= 1,000,000  

Output Format 

A single integer L - the answer to the test case

Sample Input

2 00010

Sample Output

2

Explanation

S * K = 0001000010

"1" and "10" meet the requirement that 2 * #0 <= 3 * #1 

The longest one is "10", length = 2.
"""

from bisect import bisect_left

def find_longest_valid_sequence_length(K, S):
    n = len(S)
    s = [0] * (n + 1)
    a = [0] * (n + 1)
    a[0] = (0, 0)
    
    for i in range(n):
        s[i + 1] = s[i] - 3 * (S[i] == '1') + 2 * (S[i] == '0')
        a[i + 1] = (s[i + 1], i + 1)
    
    a.sort()
    dp = [0] * (n + 1)
    dp[0] = a[0][1]
    
    for i in range(n):
        dp[i + 1] = max(dp[i], a[i + 1][1])
    
    answer = 0
    for i in range(n):
        dx = a[0][0] - s[i]
        if s[n] <= 0:
            x = K - 1
            if dx + s[n] * x > 0:
                continue
        elif dx > 0:
            continue
        else:
            x = min(K - 1, -dx // s[n])
        
        v = x * s[n] - s[i]
        p = bisect_left(a, (-v + 1, 0)) - 1
        answer = max(answer, dp[p] - i + x * n)
    
    return answer