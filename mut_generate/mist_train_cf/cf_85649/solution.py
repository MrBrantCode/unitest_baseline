"""
QUESTION:
Develop a function named `interleave_strings` that takes three string arguments and returns a new string. The new string should be constructed by interweaving characters from the input strings in a cyclic manner. The function should continue to interleave characters until all characters from the input strings have been used.
"""

def interleave_strings(str1, str2, str3):
    iters = [iter(str1), iter(str2), iter(str3)]
    result = []
    while iters:
        for i, it in enumerate(iters[:]):
            try:
                result.append(next(it))
            except StopIteration:
                iters.remove(it)
    return ''.join(result)