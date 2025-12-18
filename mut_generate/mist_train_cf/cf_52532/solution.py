"""
QUESTION:
Given a `pattern` string and a string `s`, return `true` if `s` matches the `pattern`. A string `s` matches a `pattern` if there is some bijective mapping of single characters to strings such that if each character in `pattern` is replaced by the string it maps to, then the resulting string is `s`. The mapping must satisfy two additional conditions: 
- The length of the string that a character maps to should be equal to the ASCII value of the character minus 96.
- The sum of the ASCII values of the characters in the string that a character maps to should be divisible by the ASCII value of the character.
The function to implement is `wordPatternMatch(pattern, s)`. 
Constraints: `1 <= pattern.length, s.length <= 1000` and `pattern` and `s` consist of only lower-case English letters.
"""

def wordPatternMatch(pattern, s):
    def match(p, s, dic):
        if len(p) == 0 and len(s) > 0:
            return False
        if len(p) == len(s) == 0:
            return True
        for end in range(1, len(s) + 1):
            if p[0] not in dic and s[:end] not in dic.values():
                dic[p[0]] = s[:end]
                if len(s[:end]) == ord(p[0]) - 96 and sum(ord(c) for c in s[:end]) % ord(p[0]) == 0 and match(p[1:], s[end:], dic):
                    return True
                del dic[p[0]]
            elif p[0] in dic and dic[p[0]] == s[:end] and len(s[:end]) == ord(p[0]) - 96 and sum(ord(c) for c in s[:end]) % ord(p[0]) == 0:
                if match(p[1:], s[end:], dic):
                    return True
        return False

    return match(pattern, s, {})