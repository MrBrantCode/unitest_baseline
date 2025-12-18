"""
QUESTION:
Implement a function `number_joining` that takes a list of mixed integers and lists of integers, where each inner list represents a set of options, and returns a list of strings where each string represents a combination of integers joined by dots. The function should join the first integer with each option in the first inner list, then join each of these combinations with each option in the second inner list, and so on.
"""

def number_joining(data):
    def recursive_join(data, output, current, index):
        if index < len(data):
            for i in range(len(data[index])):
                new_str = current + '.' + str(data[index][i]) if current else str(data[index][i])
                recursive_join(data, output, new_str, index + 1)
        else:
            output.append(current)
        return output
    
    output = []
    if data and isinstance(data[0], int):
        return recursive_join(data, output, str(data[0]), 1)
    else:
        return recursive_join(data, output, '', 0)