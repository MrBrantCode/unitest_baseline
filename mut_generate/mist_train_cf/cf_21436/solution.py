"""
QUESTION:
Create a context-free grammar that generates strings consisting only of a's and b's, with the same number of a's as b's, and at least one occurrence of the substring "abab".
"""

def generate_abab_string(n):
    def generate_string(n):
        if n == 0:
            return ['']
        else:
            result = []
            for s in generate_string(n-1):
                result.append('ab' + s + 'ba')
                result.append('ba' + s + 'ab')
            return result

    if n == 1:
        return ['abab']
    else:
        return ['abab' + s for s in generate_string(n-1)] + [s + 'abab' for s in generate_string(n-1)]