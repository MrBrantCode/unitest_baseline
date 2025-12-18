"""
QUESTION:
Example

Input

R?????,2?)


Output

29
"""

def evaluate_expression(expression: str) -> int:
    fm = {}
    fm[''] = -1

    def f(s):
        if s in fm:
            return fm[s]
        l = len(s)
        r = -1
        if l > 5 and s[1] in '(?' and (s[-1] in ')?'):
            if s[0] in 'R?':
                for i in range(3, l - 2):
                    if s[i] not in ',?':
                        continue
                    tl = f(s[2:i])
                    tr = f(s[i + 1:-1])
                    if tl >= 0 and tr >= 0 and (r < tr):
                        r = tr
            if s[0] in 'L?':
                for i in range(3, l - 2):
                    if s[i] not in ',?':
                        continue
                    tl = f(s[2:i])
                    tr = f(s[i + 1:-1])
                    if tl >= 0 and tr >= 0 and (r < tl):
                        r = tl
        ff = True
        if s[0] == '0' and l > 1:
            ff = False
        for tc in 'RL,()':
            if tc in s:
                ff = False
                break
        if ff:
            r = int(s.replace('?', '9'))
        fm[s] = r
        return r

    result = f(expression)
    return result if result >= 0 else -1