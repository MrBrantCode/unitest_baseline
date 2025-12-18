"""
QUESTION:
Chef recently graduated Computer Science in university, so he was looking for a job. He applied for several job offers, but he eventually settled for a software engineering job at ShareChat. Chef was very enthusiastic about his new job and the first mission assigned to him was to implement a message encoding feature to ensure the chat is private and secure.
Chef has a message, which is a string $S$ with length $N$ containing only lowercase English letters. It should be encoded in two steps as follows: 
- Swap the first and second character of the string $S$, then swap the 3rd and 4th character, then the 5th and 6th character and so on. If the length of $S$ is odd, the last character should not be swapped with any other.
- Replace each occurrence of the letter 'a' in the message obtained after the first step by the letter 'z', each occurrence of 'b' by 'y', each occurrence of 'c' by 'x', etc, and each occurrence of 'z' in the message obtained after the first step by 'a'.
The string produced in the second step is the encoded message. Help Chef and find this message.

-----Input-----
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- The second line contains the message string $S$.

-----Output-----
For each test case, print a single line containing one string — the encoded message.

-----Constraints-----
- $1 \le T \le 1,000$
- $1 \le N \le 100$
- $|S| = N$
- $S$ contains only lowercase English letters

-----Example Input-----
2
9
sharechat
4
chef

-----Example Output-----
shizxvzsg
sxuv

-----Explanation-----
Example case 1: The original message is "sharechat". In the first step, we swap four pairs of letters (note that the last letter is not swapped), so it becomes "hsraceaht". In the second step, we replace the first letter ('h') by 's', the second letter ('s') by 'h', and so on, so the resulting encoded message is "shizxvzsg".
"""

def encode_message(S: str, N: int) -> str:
    # Step 1: Swap adjacent characters
    s_list = list(S)
    for i in range(1, N, 2):
        s_list[i], s_list[i - 1] = s_list[i - 1], s_list[i]
    
    # Step 2: Replace characters with their corresponding 'a' to 'z' inverse
    for i in range(N):
        m = ord(s_list[i])
        n = ord('a')
        x = m - n
        y = n + 25 - x
        s_list[i] = chr(y)
    
    # Join the list back into a string and return
    return ''.join(s_list)