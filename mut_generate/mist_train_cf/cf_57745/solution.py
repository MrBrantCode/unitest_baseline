"""
QUESTION:
Implement a function `specialBinaryString(S)` that takes a special binary string `S` as input and returns a tuple containing the lexicographically largest special binary string possible after any number of moves, along with the number of moves required to achieve this string. 

The input string `S` has a length of at most 100 and is guaranteed to be a special binary string, where the number of 0's is equal to the number of 1's and every prefix has at least as many 1's as 0's. The number of moves required to achieve the lexicographically largest string should not exceed 1000.
"""

def makeLargestSpecial(S):
    def recursion(S):
        count = i = 0
        partition = []
        for j in range(len(S)):
            if S[j] == '1':
                count += 1
            else:
                count -= 1
            if count == 0:
                partition.append('1' + recursion(S[i + 1:j]) + '0')
                i = j + 1
        return ''.join(sorted(partition, reverse=True))
    return recursion(S), "1"