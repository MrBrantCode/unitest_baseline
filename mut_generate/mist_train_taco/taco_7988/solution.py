"""
QUESTION:
View Russian Translation

Limak is a polar bear who often chats online with his friends.
Nowadays, bears often use emoticons to express their feelings.
While most emoticons are short and boring, there is one exception.

Crying emoticon is made of any positive number of underscores between two semicolons.
So the shortest example is ;_; but it can also be e.g. ;__; or ;_____________;.

Limak sent you a message of length N consisting of underscores and semicolons.
Polar bears are easily distracted so Limak could have typed some characters by mistake.
You wonder how many ways there are to ignore some (maybe none) characters and obtain a crying emoticon.
This number could be big so find it modulo 10^9+7.

Input format:

The only line contains one string consisting of N characters, denoting a message from Limak.
Each character of string is either ; (semicolon) or _ (underscore).

Output format:

In the single line print the answer modulo 10^9+7.

Constraints:

1 ≤ N ≤ 10^5

SAMPLE INPUT
;;;;;__;_

SAMPLE OUTPUT
15

Explanation

For clarity, let's write Limak's message with spaces: ; ; ; ; ; _ _ ; _.
Note that the last underscore can't be used because there are no semicolons on the right.

Any crying emoticon must contain the last semicolon and exactly one of the first 5 semicolons.
Moreover, it must contain positive number of underscores and there are 3 ways to choose them:
1) only the first underscore
2) only the second underscore
3) first two underscores

The answer is 5*3 = 15.
"""

def count_crying_emoticons(message: str) -> int:
    MOD = 10**9 + 7
    c = 0
    rc = 0
    i = message.find(';')
    if i == -1:
        return 0
    semcols_seen = 0

    while i < len(message):
        if message[i] == '_':
            rc = (rc * 2 + semcols_seen) % MOD
        else:
            semcols_seen += 1
            c = (c + rc) % MOD
        i += 1

    return c