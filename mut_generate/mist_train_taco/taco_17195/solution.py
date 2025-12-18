"""
QUESTION:
IPL 2021 knockouts are over, teams MI, CSK, DC, and RCB are qualified for the semis. 
Today is matchday 6 and it is between Delhi Capitals and Royal Challengers Banglore. Glenn Maxwell of RCB playing flawlessly. Rishabh Pant, the new captain of the team who is also a wicket-keeper wants to send a message to the bowler. But, he can't shout message directly as a batsman can hear. So, he decided to encrypt the message by putting '*'s in the message. And this is how the bowler decrypts the message. Bowler iterates over the message string from left to right, if he finds a '*', he removes it and adds all the letters read so far to the message. He keeps on doing this till he gets rid of all the '*'. Given a decrypted message in the form of the string, the task is to find the encrypted message.
Note: If the string can be encrypted in multiple ways, find the encrypted string of smallest length.
Example 1:
Input: s = "ababcababcd"
Output: ab*c*d
Explanation: We can encrypt the string 
in following way : "ababcababcd" -> 
"ababc*d" -> "ab*c*d"
Example 2:
Input: s = "zzzzzzz"
Output: z*z*z
Explanation: The string can be encrypted 
in 2 ways: "z*z*z" and "z**zzz". Out of 
the two "z*z*z" is smaller in length.
Your Task: 
You don't need to read input or print anything. Complete the function compress() which takes the message string s as input parameter and returns the shortest possible encrypted string.
Constraints: 
1 ≤ |s| ≤ 10^{5}
"""

def encrypt_message(s: str) -> str:
    def fillarray(s, a):
        a[0] = 0
        for i in range(1, len(s)):
            series = a[i - 1]
            while series:
                if s[series] == s[i]:
                    a[i] = series + 1
                    break
                series = a[series - 1]
            if series == 0:
                a[i] = int(s[i] == s[0])
        return a

    a = [0] * len(s)
    a = fillarray(s, a)
    shortened = []
    n = len(s)
    i = n - 1
    while i > 0:
        if i % 2 == 0:
            shortened.append(s[i])
            i = i - 1
            continue
        star_here = False
        suffix = a[i]
        substrlen = i + 1
        if suffix * 2 >= substrlen:
            if substrlen % (substrlen - suffix) == 0:
                if substrlen / (substrlen - suffix) % 2 == 0:
                    star_here = True
        if star_here:
            shortened.append('*')
            i = i // 2 + 1
        else:
            shortened.append(s[i])
        i = i - 1
    ret = ''
    ret = ret + s[0]
    n = len(shortened)
    while n:
        ret = ret + shortened[n - 1]
        shortened.pop()
        n = n - 1
    return ret