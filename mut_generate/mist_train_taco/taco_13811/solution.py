"""
QUESTION:
You have been assigned to develop a filter for bad messages in the in-game chat. A message is a string $S$ of length $n$, consisting of lowercase English letters and characters ')'. The message is bad if the number of characters ')' at the end of the string strictly greater than the number of remaining characters. For example, the string ")bc)))" has three parentheses at the end, three remaining characters, and is not considered bad.


-----Input-----

The first line contains the number of test cases $t$ ($1 \leq t \leq 100$). Description of the $t$ test cases follows.

The first line of each test case contains an integer $n$ ($1 \leq n \leq 100$). The second line of each test case contains a string $S$ of length $n$, consisting of lowercase English letters and characters ')'.


-----Output-----

For each of $t$ test cases, print "Yes" if the string is bad. Otherwise, print "No".

You can print each letter in any case (upper or lower).


-----Examples-----

Input
5
2
))
12
gl))hf))))))
9
gege)))))
14
)aa))b))))))))
1
)
Output
Yes
No
Yes
Yes
Yes


-----Note-----

None
"""

def is_bad_message(S: str, n: int) -> str:
    brackets_count = 0
    i = n - 1
    
    # Count the number of ')' at the end of the string
    while i >= 0:
        if S[i] == ')':
            brackets_count += 1
        else:
            break
        i -= 1
    
    # Determine if the message is bad
    if brackets_count > n - brackets_count:
        return 'Yes'
    else:
        return 'No'