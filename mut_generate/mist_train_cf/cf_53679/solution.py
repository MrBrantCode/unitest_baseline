"""
QUESTION:
Create a function called `pack_duplicates` that takes a list as an argument and returns a new list where consecutive duplicate elements are consolidated into distinct sublists. The function should also be able to handle nested lists by recursively consolidating consecutive duplicates within the nested structures.
"""

def pack_duplicates(lst):
    def pack_helper(sublist):
        result = []
        for i in range(len(sublist)):
            if isinstance(sublist[i], list):
                result.append(pack_helper(sublist[i]))
            else:
                if i == 0 or sublist[i] != sublist[i-1]:
                    result.append([sublist[i]])
                else:
                    result[-1].append(sublist[i])
        return result

    return pack_helper(lst)