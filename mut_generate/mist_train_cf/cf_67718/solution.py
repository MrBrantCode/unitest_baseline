"""
QUESTION:
Write a function `minSwaps(str1, str2)` to determine if two given strings are permutations of each other considering case sensitivity and white spaces, and calculate the minimum number of character swaps required to transform one string into the other. The function should return -1 if the strings are not permutations of each other.
"""

def minSwaps(str1, str2):
    if len(str1) != len(str2):
        return -1

    count = [0]*256

    for i in range(len(str1)):
        count[ord(str1[i])] += 1
        count[ord(str2[i])] -= 1
    
    for i in range(256):
        if count[i] != 0:
            return -1
    
    visit = [0]*len(str1)
    answer = 0
    for i in range(len(str1)):
        if visit[i] or str1[i] == str2[i]:
            continue

        cycle_size = 0
        j = i

        while not visit[j]:
            visit[j] = 1
            j = str1.index(str2[j])
            cycle_size += 1

        if cycle_size > 0:
            answer += (cycle_size - 1)

    return answer