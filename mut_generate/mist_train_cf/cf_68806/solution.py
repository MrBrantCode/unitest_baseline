"""
QUESTION:
Write a function `deserialize(s)` that takes a string `s` representing the serialization of a nested list and returns the deserialized list. The string `s` consists of digits, square brackets `[]`, negative sign `-`, and commas `,`. The integers in the string are in binary format and need to be converted to decimal format. The length of `s` is between 1 and 5 * 10^4. The input string `s` is a valid serialization of a nested list.
"""

def deserialize(s):
    def helper(l):
        result = []
        for i in l:
            if type(i) == list:
                result.append(helper(i))
            else:
                result.append(int(str(i),2))        
        return result
    return helper(eval(s))