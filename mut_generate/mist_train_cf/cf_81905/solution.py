"""
QUESTION:
Implement a function `wordPatternMatch(pattern: str, s: str) -> bool` that returns `True` if string `s` matches the `pattern`, and `False` otherwise. A string `s` matches a `pattern` if there is a bijective mapping of single characters to strings such that if each character in `pattern` is replaced by the string it maps to, then the resulting string is `s`. The length of the string that a character maps to should be equal to the ASCII value of the character minus 96. The input constraints are `1 <= pattern.length, s.length <= 100` and both `pattern` and `s` consist of only lower-case English letters.
"""

def wordPatternMatch(pattern: str, s: str) -> bool:
    map_index = {}
    map_check = set()

    def is_match(i: int, j: int):
        if i == len(pattern):
            return j == len(s)
        if pattern[i] in map_index:
            word = map_index[pattern[i]]
            if not s.startswith(word, j):
                return False
            return is_match(i + 1, j + len(word))
        else:
            for k in range(j, len(s)):
                word = s[j: k + (ord(pattern[i]) - 96)]
                if word not in map_check:
                    map_index[pattern[i]] = word
                    map_check.add(word)
                    if is_match(i + 1, k + (ord(pattern[i]) - 96)):
                        return True
                    map_index.pop(pattern[i])
                    map_check.remove(word)
            return False

    return is_match(0, 0)