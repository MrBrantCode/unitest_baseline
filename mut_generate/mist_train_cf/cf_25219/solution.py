"""
QUESTION:
Generate a function `longest_common_substring(list1, list2)` that takes two lists of integers and returns the product of the first element of the lists and the length of their longest common substring. If the lists have no common elements, the function should return 0.
"""

def entance(list1, list2):
    longest_substring = 0
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                current_substring = 1
                k, l = i+1, j+1
                while k < len(list1) and l < len(list2) and list1[k] == list2[l]:
                    current_substring += 1
                    k += 1
                    l += 1
                longest_substring = max(longest_substring, current_substring)

    if longest_substring == 0:
        return 0
    else:
        return list1[0] * list2[0] * longest_substring