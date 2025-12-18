"""
QUESTION:
Implement a function `generate_sequence(line: str) -> str` to generate the next line in the 'look-and-say' sequence given the previous line. The 'look-and-say' sequence is a series of integers where the nth term is described by the nth-1 term, reading the previous term and describing it as the count of consecutive identical numbers followed by the number itself. For example, given '21', the next term is '1211' as it is described as 'one 2, one 1'.
"""

def generate_sequence(line: str) -> str:
    result = ""
    count = 1
    for i in range(len(line)):
        if i == len(line) - 1 or line[i] != line[i + 1]:
            result += str(count) + line[i]
            count = 1
        else:
            count += 1
    return result